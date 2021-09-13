<script>
  export let timeStamp;
  let now = new Date();

  /* Funcion para calcular diferencia de tiempo */
  // in miliseconds
  var units = {
    year: 24 * 60 * 60 * 1000 * 365,
    month: (24 * 60 * 60 * 1000 * 365) / 12,
    day: 24 * 60 * 60 * 1000,
    hour: 60 * 60 * 1000,
    minute: 60 * 1000,
    second: 1000,
  };

  /* difference between timestamp and now */
  console.log(Date(timeStamp));
  console.log(now);
  var diff = now - Date(timeStamp);
  console.log(diff);
</script>
