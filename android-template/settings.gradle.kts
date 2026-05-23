pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
    versionCatalogs {
        create("libs") {
            // Define core dependency version targets explicitly for stability
            version("androidGradlePlugin", "8.2.2")
            version("kotlin", "1.9.22")
            version("coreKtx", "1.12.0")
            version("appcompat", "1.6.1")
            version("material", "1.11.0")
            version("constraintlayout", "2.1.4")

            plugin("android-application", "com.android.application").versionRef("androidGradlePlugin")
            plugin("kotlin-android", "org.jetbrains.kotlin.android").versionRef("kotlin")
            
            library("core-ktx", "androidx.core", "core-ktx").versionRef("coreKtx")
            library("appcompat", "androidx.appcompat", "appcompat").versionRef("appcompat")
            library("material", "com.google.android.material", "material").versionRef("material")
            library("constraintlayout", "androidx.constraintlayout", "constraintlayout").versionRef("constraintlayout")
        }
    }
}

rootProject.name = "MasterAppFactoryTemplate"
include(":app")
