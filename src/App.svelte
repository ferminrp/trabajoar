<script>
	import Job from './jobs/jobPosting.svelte'
	let trabajos = []

	async function apiFetcher() {
		return fetch("https://trabajoar.ferminrp.workers.dev/")
		.then((data) => data.json()).then(function(data) {
			// For day in data append all elements to trabajos
			for (let day in data) {
				for (let work in data[day]) {
					trabajos = [...trabajos, data[day][work]];
				}
			}
			console.log(trabajos);		
		});
	}
	apiFetcher();

</script>

<main>
	<h1>#TrabajoAR</h1>
	<p>Postea en twitter usando el hashtag #TrabajoAR para aparecer!</p>
	{#each trabajos as job}
		<Job {job} />
	{/each}
</main>

<style>
	main {
		max-width: 720px;
		margin: 0 auto;
	}

	main > h1, main > p {
		color: white;;
	}
</style>