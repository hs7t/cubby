<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import L, { type LatLngBoundsExpression } from "leaflet"
    import LargeMapImg from '../../assets/Large Map.svg'
    import type { Marker } from "../../shared.svelte";

    let { markers = undefined as undefined|Array<Marker> } = $props()

    let mapElement
    let map: L.Map

    onMount(async () => {
        map = L.map('map', {
            crs: L.CRS.Simple,
            minZoom: -2,
            attributionControl: false,
        })
        let bounds: LatLngBoundsExpression = [[0, 0], [1000, 1000]]
        let image = L.imageOverlay(LargeMapImg, bounds).addTo(map)

        if (markers != undefined) {
            for (let marker of markers) {
                L.marker(marker.coordinates).addTo(map);
            }
        }
        
        map.fitBounds(bounds);
    })

    onDestroy(async () => {
        if (map) {
            console.log("Unloading map!")
            map.remove()
        }
    })
</script>

<div id="map" bind:this={mapElement}>
</div>

<style>
    #map {
        height: min(100cqw, 100cqh);
        width: min(100cqw, 100cqh);
        aspect-ratio: 1 / 1;
    }
</style>