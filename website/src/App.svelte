<script lang="ts">
    import Map from "./lib/components/Map.svelte";
  import RandomStringClicker from "./lib/components/RandomStringClicker.svelte";
    import Header from "./lib/sections/Header.svelte"
    import Navigation from "./lib/sections/Navigation.svelte";
</script>

<main>
    <span class="group first-group">
        <Header></Header>
        <Map markers={[
            { coordinates: [500, 500], title: "Meow", action: () => { console.log("I was clicked!") }, id: "testMarker" }
        ]}></Map>
        <RandomStringClicker strings={["It's cold outside. Fancy some websites?"]}></RandomStringClicker>
    </span>
    <span class="group second-group">
        <Navigation></Navigation>
    </span>
</main>

<style>
    :global(body) {
        font-family: var(--c-font-family-primary);
        font-size: var(--c-font-size-A);
        background-color: var(--c-color-background-A);
        color: var(--c-color-primary);
    }

    :global(::selection) {
        background-color: var(--c-color-primary);
        color: var(--c-color-background-A);
    }

    :global(#app) {
        width: 100dvw;
        height: 100dvh;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    main {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;

        gap: 2rem;
        height: 80%;
        width: 80%;

        max-width: 1000px;
    }

    .group {
        display: flex;
        flex-grow: 1;
        flex-shrink: 1;
        gap: 1em;
        flex-direction: column;
        max-height: 100%;
    }

    .first-group {
        justify-content: space-between;
    }

    :global(section), .group {
        flex-grow: 1;
    }
</style>
