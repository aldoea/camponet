var db = camponetFirestore;
var citiesRef = db.collection("cities");

function addUser() {
    let first = document.getElementById('first').value;
    let last = document.getElementById('last').value;
    let born = parseInt(document.getElementById('born').value);
    db.collection("users").add({
        first: first,
        last: last,
        born: born
    })
    .then(function(docRef) {
        console.log("Document written with ID: ", docRef.id);
        return false;
    })
    .catch(function(error) {
        console.error("Error adding document: ", error);
    });
}

// Loads chat messages history and listens for upcoming ones.
function loadUsers() {
    var users = []
    var usersCtrl = new Vue({
        el: "#usersList",
        data: {
          users: users
        }
    });
    // Create the query to load the last 12 messages and listen for new ones.
    let query = db.collection('users')
        .orderBy('born', 'desc')
        .limit(5);
    
    // Start listening to the query.
    query.onSnapshot(function(snapshot) {
        snapshot.docChanges().forEach(function(change) {
        if (change.type === "added") {
            let user = change.doc.data();
            users.push(user);
        }
        });
    });
}

loadUsers();