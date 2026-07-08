package com.security.phonedefender

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.security.phonedefender.ui.theme.PhoneDefenderTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            PhoneDefenderTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    MainScreen()
                }
            }
        }
    }
}

@Composable
fun MainScreen() {
    var selectedTab by remember { mutableStateOf(0) }
    
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(
                brush = Brush.verticalGradient(
                    colors = listOf(
                        Color(0xFF0D47A1),
                        Color(0xFF1565C0),
                        Color(0xFF1976D2)
                    )
                )
            )
    ) {
        // Header
        HeaderSection()
        
        // Tab Navigation
        TabRow(
            selectedTabIndex = selectedTab,
            modifier = Modifier.fillMaxWidth(),
            containerColor = Color(0xFF1565C0),
            contentColor = Color.White
        ) {
            Tab(
                selected = selectedTab == 0,
                onClick = { selectedTab = 0 },
                icon = { Icon(Icons.Filled.Security, null) },
                text = { Text("Security") }
            )
            Tab(
                selected = selectedTab == 1,
                onClick = { selectedTab = 1 },
                icon = { Icon(Icons.Filled.Wifi, null) },
                text = { Text("Network") }
            )
            Tab(
                selected = selectedTab == 2,
                onClick = { selectedTab = 2 },
                icon = { Icon(Icons.Filled.Apps, null) },
                text = { Text("Apps") }
            )
        }
        
        // Tab Content
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp)
        ) {
            when (selectedTab) {
                0 -> SecurityTab()
                1 -> NetworkTab()
                2 -> AppsTab()
            }
        }
    }
}

@Composable
fun HeaderSection() {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            "🛡️ Phone Defender",
            fontSize = 32.sp,
            color = Color.White,
            fontWeight = androidx.compose.ui.text.font.FontWeight.Bold
        )
        Text(
            "Premium Security Suite v1.0",
            fontSize = 14.sp,
            color = Color(0xFFB3E5FC),
            modifier = Modifier.padding(top = 8.dp)
        )
    }
}

@Composable
fun SecurityTab() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        SecurityCard(
            title = "Malware Scanner",
            status = "✓ Safe",
            icon = Icons.Filled.Security,
            description = "No threats detected"
        )
        SecurityCard(
            title = "Password Strength",
            status = "Strong",
            icon = Icons.Filled.Lock,
            description = "All passwords are secure"
        )
        SecurityCard(
            title = "File Encryption",
            status = "Active",
            icon = Icons.Filled.VpnLock,
            description = "3 files encrypted"
        )
    }
}

@Composable
fun NetworkTab() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        SecurityCard(
            title = "WiFi Monitor",
            status = "WPA2",
            icon = Icons.Filled.Wifi,
            description = "Connected to secure network"
        )
        SecurityCard(
            title = "Network Traffic",
            status = "Monitoring",
            icon = Icons.Filled.VisibilityOff,
            description = "12 active connections"
        )
    }
}

@Composable
fun AppsTab() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        SecurityCard(
            title = "App Tracker",
            status = "48 Apps",
            icon = Icons.Filled.Apps,
            description = "All apps monitored"
        )
        SecurityCard(
            title = "Permission Monitor",
            status = "Active",
            icon = Icons.Filled.PrivacyTip,
            description = "8 apps requesting permissions"
        )
    }
}

@Composable
fun SecurityCard(
    title: String,
    status: String,
    icon: androidx.compose.material.icons.Icons,
    description: String
) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .height(120.dp),
        colors = CardDefaults.cardColors(
            containerColor = Color.White.copy(alpha = 0.95f)
        ),
        elevation = CardDefaults.cardElevation(defaultElevation = 8.dp)
    ) {
        Row(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            Column(
                modifier = Modifier.weight(1f)
            ) {
                Text(
                    title,
                    fontSize = 16.sp,
                    fontWeight = androidx.compose.ui.text.font.FontWeight.Bold,
                    color = Color(0xFF1565C0)
                )
                Text(
                    description,
                    fontSize = 12.sp,
                    color = Color.Gray,
                    modifier = Modifier.padding(top = 4.dp)
                )
            }
            Column(
                horizontalAlignment = Alignment.End
            ) {
                Icon(
                    icon,
                    contentDescription = null,
                    tint = Color(0xFF1565C0),
                    modifier = Modifier.size(32.dp)
                )
                Text(
                    status,
                    fontSize = 14.sp,
                    fontWeight = androidx.compose.ui.text.font.FontWeight.Bold,
                    color = Color(0xFF00B050),
                    modifier = Modifier.padding(top = 4.dp)
                )
            }
        }
    }
}

@Composable
fun rememberScrollState(): androidx.compose.foundation.ScrollState {
    return remember { androidx.compose.foundation.ScrollState(0) }
}