<script lang="ts">
    import Map from "./lib/components/Map.svelte";
    import Header from "./lib/sections/Header.svelte"
    import Navigation from "./lib/sections/Navigation.svelte";
</script>

<main>
    <Header></Header>

    <Map markers={[
        { coordinates: [500, 500], title: "Meow", action: () => { console.log("I was clicked!") }, id: "testMarker" }
    ]}></Map>

    <Navigation></Navigation>
</main>

<style>
    :global(body) {
        font-family: var(--c-font-family-primary);
        font-size: var(--c-font-size-A);
        background-color: var(--c-color-background-A);
        color: var(--c-color-primary);
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
