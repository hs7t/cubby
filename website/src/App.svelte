<script lang="ts">
  import Map from "./lib/components/Map.svelte";

</script>

<main>
    <Map markers={[
        { coordinates: [500, 500], title: "Meow", action: () => { console.log("I was clicked!") }, id: "testMarker" }
    ]}></Map>
</main>

<style>
  :global(body) {
    font-family: var(--c-font-family-pri);
  }
</style>
