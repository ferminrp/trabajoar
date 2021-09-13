<script>
	import Job from './jobs/jobPosting.svelte';
	import { BarLoader } from 'svelte-loading-spinners';
	let trabajos = []
	let loading = true;

	async function apiFetcher() {
		return fetch("https://trabajoar.ferminrp.workers.dev/")
		.then((data) => data.json()).then(function(data) {
			// For day in data append all elements to trabajos
			for (let day in data) {
				for (let work in data[day]) {
					trabajos = [...trabajos, data[day][work]];
				}
			}
			// Sort trabajos by "created_at" key
			trabajos = trabajos.sort((a, b) => (a.created_at > b.created_at) ? -1 : 1);
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
	<p>Postea en twitter usando los hashtags #TrabajoAR o #LaburosAr para aparecer!</p>
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

	main > h1, main > p {
		color: white;;
	}

	.barloader {
		width: 100%;
		height: 50vh;
		display: flex;
		justify-content: center;
		align-items: center;
	}

</style>