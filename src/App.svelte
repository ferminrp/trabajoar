<script>
  import Job from "./jobs/jobPosting.svelte";
  import { BarLoader } from "svelte-loading-spinners";
  let trabajos = [];
  let loading = true;

  async function apiFetcher() {
    var myHeaders = new Headers();
    myHeaders.append(
      "apikey",
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTU2NTMxNywiZXhwIjoxOTQ3MTQxMzE3fQ.vNZUmP1dGVKLTZBlNfKf-ZzHi7af5bmZ03bJZnzPPrg"
    );
    myHeaders.append(
      "Authorization",
      "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTU2NTMxNywiZXhwIjoxOTQ3MTQxMzE3fQ.vNZUmP1dGVKLTZBlNfKf-ZzHi7af5bmZ03bJZnzPPrg"
    );

    var requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow",
    };

	const yourDate = new Date();
	yourDate.setDate(yourDate.getDate() - 1)
	let dateString = yourDate.toISOString().split('T')[0];
	console.log(dateString);

    return fetch("https://qegerxvnmsvqhoxidyzq.supabase.co/rest/v1/tweets?select=*&created_date=gte."+dateString+"&order=created_date.desc&limit=1000", requestOptions)
      .then((data) => data.json())
      .then(function (data) {
        // For day in data append all elements to trabajos

        for (let work in data) {
        	trabajos = [...trabajos, data[work]];
        }
        
        // Sort trabajos by "created_at" key
        trabajos = trabajos.sort((a, b) =>
          a.created_at > b.created_at ? -1 : 1
        );
        loading = false;
        console.log(trabajos);
      });
  }
  apiFetcher();
</script>

<main>
  {#if loading}
    <div class="barloader">
      <BarLoader color="#4C6BAE" />
    </div>
  {:else}
    <h1>#TrabajoAR</h1>
    <p>
      Postea en twitter usando los hashtags #TrabajoAR o #LaburosAr para
      aparecer!
    </p>
    {#each trabajos as job}
      <Job {job} />
    {/each}
  {/if}
</main>

<style>
  main {
    width: 720px;
    margin: 0 auto;
    max-width: 90vw;
    padding-bottom: 5rem;
  }

  main > h1,
  main > p {
    color: white;
  }

  .barloader {
    width: 100%;
    height: 50vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
