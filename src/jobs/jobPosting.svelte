<script>
  import Author from "./Author.svelte";
  export let job;

  let username = job["author"][0]["username"];
  let id = job["id"];

  let url = "https://www.twitter.com/" + username + "/status/" + id;
</script>

<article>
  <Author authorData={job.author} />
  <p>{job["text"]}</p>
  <a href={url}>Ver Publicación</a>
</article>

<style>
  article {
    background-color: #1a1b45;
    border-radius: 10px;
    padding: 2rem;
    box-sizing: border-box;
    margin-bottom: 2rem;
    color: white;
  }

  a {
    background-color: #4c6bae;
    border: none;
    color: white;
    text-decoration: none;
    border-radius: 0.5rem;
    padding: 0.5rem 2rem;
    box-sizing: border-box;
    margin-top: 2rem;
    cursor: pointer;
    display: inline-block;
  }
</style>
