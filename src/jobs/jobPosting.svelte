<script>
  import Author from "./Author.svelte";
  import TimeDiff from "./TimeDiff.svelte";
  import Tags from "./Tags.svelte";
  export let job;

  let username = job["author"]["username"];
  let id = job["id"];
  let timeStamp = job["created_date"];
  let tags = job["entities"]["hashtags"];
  let imageUrl = '';

  try {
    imageUrl = job["attachments"]["url"];
    console.log(imageUrl);
  } catch (error) {}

  let url = "https://www.twitter.com/" + username + "/status/" + id;
</script>

<article>
  <Author authorData={job.author} />
  <p>{job["text"]}</p>
  {#if imageUrl}
  <img src={imageUrl} />
  {/if}
  <Tags {tags} />
  <a target="_blank" href={url}>Ver Publicación</a>
  <TimeDiff {timeStamp} />
</article>

<style>
  article {
    background-color: #1a1b45;
    border-radius: 10px;
    padding: 2rem;
    box-sizing: border-box;
    margin-bottom: 2rem;
    color: white;
    position: relative;
  }

  a {
    background-color: #4c6bae;
    border: none;
    color: white;
    text-decoration: none;
    border-radius: 0.5rem;
    padding: 0.5rem 2rem;
    box-sizing: border-box;
    cursor: pointer;
    display: inline-block;
    margin-top: 2rem;
  }

  img {
    width: 100%;
    margin-top: 1rem;
    margin-bottom: 1rem;
    border-radius: 5px;
    opacity: 89%;
  }
</style>
