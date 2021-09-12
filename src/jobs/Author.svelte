<script>
    export let authorData;

    let username = authorData[0]["username"];
    let imageUrl = authorData[0]["profile_image_url"];
    let profileUrl = "https://twitter.com/"+username;
</script>

<a href="">
    <img src="{imageUrl}" alt="">
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