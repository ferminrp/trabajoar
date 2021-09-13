<script>
  export let timeStamp;
  $: croppedTimeStamp = timeStamp.substring(0, 10)
</script>

<p>{croppedTimeStamp}</p>

<style>
  p {
    font-size: 0.8rem;
    color: #535cc7;
    margin: 0px;
    position: absolute;
    top: 1rem;
    right: 1rem;
  }
</style>
