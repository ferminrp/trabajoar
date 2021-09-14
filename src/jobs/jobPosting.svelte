<script>
  import Author from "./Author.svelte";
  import TimeDiff from "./TimeDiff.svelte";
  import Tags from "./Tags.svelte";
  export let job;

  let urlRegex =
    /(\b((https?|ftp|file):\/\/)?((([a-z\d]([a-z\d-]*[a-z\d])*)\.)+[a-z]{2,}|((\d{1,3}\.){3}\d{1,3}))(\:\d+)?(\/[-a-z\d%_.~+]*)*(\?[;&a-z\d%_.~+=-]*)?(\#[-a-z\d_]*)?)/gi;

  let username = job["author"]["username"];
  let id = job["id"];
  let timeStamp = job["created_date"];
  let tags = job["entities"]["hashtags"];
  let imageUrl = "";

  let text = job["text"].replace(urlRegex, function (url) {
    var newUrl = url.indexOf("http") === -1 ? "http://" + url : url;
    return '<a href="' + newUrl + '">' + url + "</a>";
  });

  try {
    imageUrl = job["attachments"]["url"];
  } catch (error) {}

  let url = "https://www.twitter.com/" + username + "/status/" + id;
</script>

<article>
  <Author authorData={job.author} />
  <p>{@html text}</p>
  {#if imageUrl}
    <img loading="lazy" src={imageUrl} />
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
