plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.ssafy.firstsubject"
    compileSdk = 33

    defaultConfig {
        applicationId = "com.ssafy.firstsubject"
        minSdk = 24
        targetSdk = 33
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    kotlinOptions {
        jvmTarget = "1.8"
    }
    viewBinding{
        enable = true
    }

}

dependencies {

    implementation("androidx.core:core-ktx:1.9.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("com.google.android.material:material:1.8.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.1.5")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")

    // https://github.com/square/retrofit
    implementation ("com.squareup.retrofit2:retrofit:2.9.0")

    // https://github.com/square/okhttp
    implementation("com.squareup.okhttp3:okhttp:4.9.0")

    // https://github.com/square/retrofit/tree/master/retrofit-converters/gson
    implementation ("com.squareup.retrofit2:converter-gson:2.9.0")

    // https://github.com/square/okhttp/tree/master/okhttp-logging-interceptor
    implementation("com.squareup.okhttp3:logging-interceptor:4.9.0")

    // 코루틴
    implementation ("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2")
    implementation ("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.5.2")

    //viewmodel dependency 추가
    implementation ("androidx.lifecycle:lifecycle-viewmodel-ktx:2.4.1")
    //lifecycle scope dependency
    implementation ("androidx.lifecycle:lifecycle-runtime-ktx:2.4.1")
    //framework ktx dependency 추가
    implementation ("androidx.fragment:fragment-ktx:1.5.4")
}