<script>
    export let authorData;

    let username = authorData["username"];
    let imageUrl = authorData["profile_image_url"];
    let profileUrl = "https://twitter.com/"+username;
</script>

<a href="{profileUrl}">
    <img loading="lazy" src="{imageUrl}" alt="">
    <h3>{username}</h3>
</a>

<style>
    a {
        color: white;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    img {
        border-radius: 50%;
    }
</style>