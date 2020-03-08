// TODO: Replace the following with your app's Firebase project configuration
// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyDSaunH3A-Qa_qAqU5yzyCoxbxz38LugYQ",
    authDomain: "campo-net2020.firebaseapp.com",
    databaseURL: "https://campo-net2020.firebaseio.com",
    projectId: "campo-net2020",
    storageBucket: "campo-net2020.appspot.com",
    messagingSenderId: "129438672184",
    appId: "1:129438672184:web:f8931f1a178a5c2fbc8dcd",
    measurementId: "G-G276GXVLP1"
};
// Initialize Firebase
if (!firebase.apps.length) {
    
    var camponet = firebase.initializeApp(firebaseConfig);
    console.log(camponet.name);  // "[camponet]"
    
    // Option 1: Access Firebase services via the camponet variable
    var analytics = firebase.analytics();
    var camponetFirestore = camponet.firestore();
}
