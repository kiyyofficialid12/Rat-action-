#!/bin/bash

# Phone Defender - Build Script
# Complete build automation

set -e

echo "🔨 Phone Defender - Build System"
echo "================================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

check_java() {
    if ! command -v java &> /dev/null; then
        log_error "Java not found. Please install Java 11+"
        exit 1
    fi
    JAVA_VERSION=$(java -version 2>&1 | grep -oP '(?<=").*?(?=")' | head -1)
    log_info "Java version: $JAVA_VERSION"
}

check_android_sdk() {
    if [ -z "$ANDROID_HOME" ]; then
        log_error "ANDROID_HOME not set. Please set ANDROID_HOME environment variable."
        exit 1
    fi
    log_info "Android SDK: $ANDROID_HOME"
}

build_debug() {
    log_info "Building Debug APK..."
    ./gradlew clean assembleDebug --stacktrace
    log_info "Debug APK: app/build/outputs/apk/debug/app-debug.apk"
}

build_release() {
    log_info "Building Release APK..."
    ./gradlew clean assembleRelease --stacktrace
    log_info "Release APK: app/build/outputs/apk/release/app-release.apk"
}

build_bundle() {
    log_info "Building Android App Bundle..."
    ./gradlew bundleRelease --stacktrace
    log_info "Bundle: app/build/outputs/bundle/release/app-release.aab"
}

run_tests() {
    log_info "Running Unit Tests..."
    ./gradlew testDebugUnitTest
}

run_lint() {
    log_info "Running Lint Analysis..."
    ./gradlew lint
}

install_debug() {
    log_info "Installing Debug APK on connected device..."
    ./gradlew installDebug
}

install_release() {
    log_warn "Installing Release APK (requires signing)"
    ./gradlew installRelease
}

clean() {
    log_info "Cleaning build files..."
    ./gradlew clean
}

full_build() {
    log_info "Running full build pipeline..."
    check_java
    check_android_sdk
    clean
    run_tests
    run_lint
    build_debug
    build_release
    build_bundle
    log_info "✅ Full build completed successfully!"
}

# Main
case "${1:-help}" in
    debug)
        check_java
        check_android_sdk
        build_debug
        ;;
    release)
        check_java
        check_android_sdk
        build_release
        ;;
    bundle)
        check_java
        check_android_sdk
        build_bundle
        ;;
    test)
        check_java
        run_tests
        ;;
    lint)
        check_java
        run_lint
        ;;
    install-debug)
        check_java
        install_debug
        ;;
    install-release)
        check_java
        install_release
        ;;
    clean)
        clean
        ;;
    full)
        full_build
        ;;
    help|*)
        echo "Usage: ./build.sh [command]"
        echo ""
        echo "Commands:"
        echo "  debug          Build debug APK"
        echo "  release        Build release APK"
        echo "  bundle         Build Android App Bundle"
        echo "  test           Run unit tests"
        echo "  lint           Run lint analysis"
        echo "  install-debug  Install debug APK on device"
        echo "  install-release Install release APK on device"
        echo "  clean          Clean build files"
        echo "  full           Run complete build pipeline"
        echo "  help           Show this help message"
        echo ""
        echo "Example: ./build.sh debug"
        ;;
esac
