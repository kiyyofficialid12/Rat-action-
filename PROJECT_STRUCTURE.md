# Phone Defender - Project Structure

```
Rat-action-/
├── .github/
│   └── workflows/
│       └── build-apk.yml           # GitHub Actions CI/CD
│
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── kotlin/com/security/phonedefender/
│   │   │   │   ├── MainActivity.kt              # Main activity
│   │   │   │   ├── ui/
│   │   │   │   │   ├── screens/                # Screen components
│   │   │   │   │   │   ├── SecurityScreen.kt
│   │   │   │   │   │   ├── NetworkScreen.kt
│   │   │   │   │   │   ├── AppsScreen.kt
│   │   │   │   │   │   └── SettingsScreen.kt
│   │   │   │   │   ├── components/             # Reusable components
│   │   │   │   │   │   ├── SecurityCard.kt
│   │   │   │   │   │   ├── NetworkMonitor.kt
│   │   │   │   │   │   └── PermissionRequest.kt
│   │   │   │   │   └── theme/
│   │   │   │   │       ├── Color.kt
│   │   │   │   │       ├── Typography.kt
│   │   │   │   │       └── Theme.kt
│   │   │   │   ├── viewmodels/                # ViewModels (MVVM)
│   │   │   │   │   ├── SecurityViewModel.kt
│   │   │   │   │   ├── NetworkViewModel.kt
│   │   │   │   │   └── AppViewModel.kt
│   │   │   │   ├── services/                  # Background services
│   │   │   │   │   ├── MalwareScanService.kt
│   │   │   │   │   ├── NetworkMonitorService.kt
│   │   │   │   │   └── AppTrackerService.kt
│   │   │   │   ├── repositories/              # Data repositories
│   │   │   │   │   ├── SecurityRepository.kt
│   │   │   │   │   └── NetworkRepository.kt
│   │   │   │   ├── data/                      # Data models
│   │   │   │   │   ├── dao/
│   │   │   │   │   ├── entity/
│   │   │   │   │   └── database/
│   │   │   │   └── utils/                     # Utilities
│   │   │   │       ├── Encryption.kt
│   │   │   │       ├── PermissionHelper.kt
│   │   │   │       └── SystemUtils.kt
│   │   │   ├── res/
│   │   │   │   ├── drawable/                 # App icons & images
│   │   │   │   ├── values/
│   │   │   │   │   ├── colors.xml
│   │   │   │   │   ├── strings.xml
│   │   │   │   │   └── themes.xml
│   │   │   │   └── menu/
│   │   │   └── AndroidManifest.xml
│   │   ├── test/
│   │   │   └── java/com/security/phonedefender/
│   │   │       ├── SecurityTest.kt
│   │   │       └── NetworkTest.kt
│   │   └── androidTest/
│   │       └── java/com/security/phonedefender/
│   │           └── MainActivityTest.kt
│   ├── build.gradle                          # App-level build config
│   └── proguard-rules.pro                    # ProGuard rules
│
├── .github/
│   └── workflows/
│       └── build-apk.yml
│
├── build.gradle                              # Project-level build config
├── settings.gradle                           # Gradle settings
├── build.sh                                  # Build script
├── gradlew                                   # Gradle wrapper
├── gradlew.bat                               # Gradle wrapper (Windows)
│
├── README.md                                 # Project documentation
├── INSTALL_GUIDE.md                          # Installation guide
├── DEPENDENCIES.md                           # Dependencies & setup
├── SECURITY_POLICY.md                        # Security policy
├── LICENSE                                   # MIT License
└── .gitignore                                # Git ignore rules
```

## Architecture Overview

```
┌─────────────────────────────────────┐
│       Jetpack Compose UI            │
│  (MainActivity, Screens, Components) │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      ViewModels (MVVM Pattern)      │
│  (SecurityVM, NetworkVM, AppVM)     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│     Repositories & Services         │
│  (Data access & business logic)     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Local Storage & Database       │
│  (Room, SharedPreferences, Files)   │
└─────────────────────────────────────┘
```

## Build Artifacts

After building, find:

- **Debug APK:** `app/build/outputs/apk/debug/app-debug.apk`
- **Release APK:** `app/build/outputs/apk/release/app-release.apk`
- **Bundle:** `app/build/outputs/bundle/release/app-release.aab`
- **Test Reports:** `app/build/reports/`
- **Lint Reports:** `app/build/reports/lint-results*.html`

## Gradle Tasks

```bash
./gradlew tasks                    # List all tasks
./gradlew assembleDebug            # Build debug APK
./gradlew assembleRelease          # Build release APK
./gradlew bundleRelease            # Build app bundle
./gradlew test                     # Run tests
./gradlew lint                     # Run lint analysis
./gradlew installDebug             # Install on device
./gradlew clean                    # Clean build
```
