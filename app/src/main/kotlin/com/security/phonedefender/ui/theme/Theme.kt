package com.security.phonedefender.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val DarkColorScheme = darkColorScheme(
    primary = Color(0xFF1565C0),
    primaryContainer = Color(0xFF1976D2),
    secondary = Color(0xFF03DAC6),
    tertiary = Color(0xFF03DAC6),
    background = Color(0xFF121212),
    surface = Color(0xFF1E1E1E),
    error = Color(0xFFB00020),
    onPrimary = Color.White,
    onSecondary = Color.Black,
    onBackground = Color.White,
    onSurface = Color.White,
    onError = Color.White,
)

private val LightColorScheme = lightColorScheme(
    primary = Color(0xFF1565C0),
    primaryContainer = Color(0xFF1976D2),
    secondary = Color(0xFF03DAC6),
    tertiary = Color(0xFF03DAC6),
    background = Color(0xFFFAFAFA),
    surface = Color.White,
    error = Color(0xFFB00020),
    onPrimary = Color.White,
    onSecondary = Color.Black,
    onBackground = Color.Black,
    onSurface = Color.Black,
    onError = Color.White,
)

@Composable
fun PhoneDefenderTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        content = content
    )
}

object Typography {
    val displayLarge = androidx.compose.material3.Typography().displayLarge
    val displayMedium = androidx.compose.material3.Typography().displayMedium
    val displaySmall = androidx.compose.material3.Typography().displaySmall
    val headlineLarge = androidx.compose.material3.Typography().headlineLarge
    val headlineMedium = androidx.compose.material3.Typography().headlineMedium
    val headlineSmall = androidx.compose.material3.Typography().headlineSmall
    val titleLarge = androidx.compose.material3.Typography().titleLarge
    val titleMedium = androidx.compose.material3.Typography().titleMedium
    val titleSmall = androidx.compose.material3.Typography().titleSmall
    val bodyLarge = androidx.compose.material3.Typography().bodyLarge
    val bodyMedium = androidx.compose.material3.Typography().bodyMedium
    val bodySmall = androidx.compose.material3.Typography().bodySmall
    val labelLarge = androidx.compose.material3.Typography().labelLarge
    val labelMedium = androidx.compose.material3.Typography().labelMedium
    val labelSmall = androidx.compose.material3.Typography().labelSmall
}