<script>
  import Tag from "../UI/Tag.svelte";
  export let tags = [];
</script>

<div>
  {#each tags as tag, i (tag)}
    <Tag tag={tag["tag"]} />
  {/each}
</div>


<style>
    div {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
    }
</style>
