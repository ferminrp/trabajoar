/* Get data from firebase API */
const rawData = fetch("https://trabajoar-d6c63-default-rtdb.firebaseio.com/.json")
.then((resp) => resp.json())
.then(function(data) {
    console.log(data);
})