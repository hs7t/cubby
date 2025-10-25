<script lang="ts">
    import Map from "./lib/components/Map.svelte";
    import Header from "./lib/sections/Header.svelte"
</script>

<main>
    <Header></Header>

    <Map markers={[
        { coordinates: [500, 500], title: "Meow", action: () => { console.log("I was clicked!") }, id: "testMarker" }
    ]}></Map>
</main>

<style>
    :global(body) {
        font-family: var(--c-font-family-primary);
    }

    :global(#app) {
        width: clamp(40vw, 500px, 90vw);
        margin: auto;
    }

    main {
        width: 100%;
        display: flex;
        flex-direction: column;

        gap: 2rem;
        padding: 10%;
    }
</style>
