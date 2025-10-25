<script lang="ts">
  import Map from "./lib/components/Map.svelte";

</script>

<main>
    <Map markers={[
        { coordinates: [500, 500], title: "Meow", action: () => {}  }
    ]}></Map>
</main>

<style>
</style>
