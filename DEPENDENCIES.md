# 📱 Phone Defender - Requirements & Dependencies

## System Requirements

### Development
- **Java:** JDK 11 or higher
- **Android SDK:** API 34 (Android 14)
- **Gradle:** 8.0+
- **RAM:** 8GB+ recommended
- **Storage:** 10GB+ for SDK and builds
- **OS:** Linux, macOS, or Windows (WSL2)

### Runtime (Android Device)
- **API Level:** 24+ (Android 7.0 Nougat)
- **RAM:** 2GB minimum, 4GB+ recommended
- **Storage:** 100MB free space
- **Permissions:** As per AndroidManifest.xml

---

## Dependencies

### Core Android Libraries
```gradle
# AndroidX
androidx.core:core-ktx:1.12.0
androidx.appcompat:appcompat:1.6.1
androidx.constraintlayout:constraintlayout:2.1.4

# Material Design 3
com.google.android.material:material:1.11.0
```

### Jetpack Compose UI
```gradle
androidx.compose.ui:ui:1.6.0
androidx.compose.material3:material3:1.2.0
androidx.compose.material:material-icons-extended:1.6.0
androidx.activity:activity-compose:1.8.0
androidx.lifecycle:lifecycle-runtime-ktx:2.6.2
androidx.lifecycle:lifecycle-viewmodel-compose:2.6.2
```

### Navigation
```gradle
androidx.navigation:navigation-compose:2.7.5
```

### Asynchronous Programming
```gradle
org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3
org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3
```

### Local Database
```gradle
androidx.room:room-runtime:2.6.1
androidx.room:room-ktx:2.6.1
kapt androidx.room:room-compiler:2.6.1
```

### Security & Encryption
```gradle
androidx.security:security-crypto:1.1.0-alpha06
org.bouncycastle:bcprov-jdk15on:1.70
```

### Networking
```gradle
com.squareup.okhttp3:okhttp:4.11.0
com.squareup.retrofit2:retrofit:2.9.0
com.squareup.retrofit2:converter-gson:2.9.0
```

### JSON Processing
```gradle
com.google.code.gson:gson:2.10.1
```

### Image Loading
```gradle
io.coil-kt:coil-compose:2.5.0
```

### Analytics & Charts
```gradle
com.github.PhilJay:MPAndroidChart:v3.1.0
```

### Animations
```gradle
com.airbnb.android:lottie-compose:6.1.0
```

### Permissions & System UI
```gradle
com.google.accompanist:accompanist-permissions:0.33.2-alpha
com.google.accompanist:accompanist-systemuicontroller:0.33.2-alpha
```

### Testing
```gradle
testImplementation junit:junit:4.13.2
androidTestImplementation androidx.test.ext:junit:1.1.5
androidTestImplementation androidx.test.espresso:espresso-core:3.5.1
```

---

## Build Configuration

### Gradle Build Tools
```gradle
android {
    compileSdk 34
    
    defaultConfig {
        applicationId "com.security.phonedefender"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0.0"
    }
}
```

### ProGuard Rules
```proguard
-keep class com.security.phonedefender.** { *; }
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    !static !transient <fields>;
    !private <fields>;
    !private <methods>;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
    java.lang.Object writeReplace();
    java.lang.Object readResolve();
}
```

---

## Setup Instructions

### 1. Install Prerequisites

**macOS:**
```bash
brew install java11
brew install android-sdk
brew install gradle
```

**Ubuntu/Debian:**
```bash
sudo apt-get install openjdk-11-jdk
sudo apt-get install android-sdk
sudo apt-get install gradle
```

**Windows (with Chocolatey):**
```powershell
choco install jdk11
choco install android-sdk
choco install gradle
```

### 2. Setup Android SDK

```bash
# Set ANDROID_HOME
export ANDROID_HOME=/path/to/android/sdk

# Install required SDK components
$ANDROID_HOME/tools/bin/sdkmanager "platforms;android-34"
$ANDROID_HOME/tools/bin/sdkmanager "build-tools;34.0.0"
$ANDROID_HOME/tools/bin/sdkmanager "system-images;android-34;google_apis;x86_64"
```

### 3. Clone Repository

```bash
git clone https://github.com/kiyyofficialid12/Rat-action-.git
cd Rat-action-
```

### 4. Build APK

```bash
# Debug APK
./gradlew assembleDebug

# Release APK (requires keystore)
./gradlew assembleRelease

# Clean build
./gradlew clean assembleDebug
```

### 5. Install on Device

```bash
# Via ADB
adb install app/build/outputs/apk/debug/app-debug.apk

# Via Gradle
./gradlew installDebug
```

---

## Troubleshooting

### Gradle Build Errors

**Error: "Unable to find method 'compile()' for argument"**
```bash
# Solution: Update Gradle
./gradlew wrapper --gradle-version=8.2.1
```

**Error: "SDK location not found"**
```bash
# Solution: Create local.properties
echo "sdk.dir=/path/to/android/sdk" > local.properties
```

**Error: "Duplicate class" (MultiDex)**
```gradle
# Add to build.gradle
android {
    defaultConfig {
        multiDexEnabled true
    }
}
```

### Memory Issues

```bash
# Increase Gradle heap size
export GRADLE_OPTS="-Xmx4g"
```

### Device Connection

```bash
# List connected devices
adb devices

# Enable USB debugging
adb shell setprop persist.service.usb.config mtp,adb

# Reconnect device
adb reconnect
```

---

## Performance Optimization

### Build Speed

```gradle
android {
    buildTypes {
        debug {
            minifyEnabled false
            shrinkResources false
        }
    }
}
```

### Runtime Performance

- Enable R8 code shrinking
- Use ProGuard obfuscation
- Optimize drawable resources
- Enable vectorDrawable support

---

## CI/CD Integration

### GitHub Actions
See `.github/workflows/build-apk.yml`

### Local Testing

```bash
# Run unit tests
./gradlew test

# Run instrumented tests
./gradlew connectedAndroidTest

# Run lint
./gradlew lint
```

---

## Version History

| Version | Date | Changes |
|---------|------|----------|
| 1.0.0 | 2024 | Initial release |

---

**📝 Last Updated:** 2024
**🔧 Maintained by:** Phone Defender Team