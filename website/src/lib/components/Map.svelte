<script lang="ts">
    import L, { type LatLngBoundsExpression } from "leaflet"
    import LargeMapImg from '../../assets/Large Map.svg'

    let mapElement

    let map = L.map('map', {
        crs: L.CRS.Simple
    });
    let bounds: LatLngBoundsExpression = [[0, 0], [1000, 1000]]
    let image = L.imageOverlay(LargeMapImg, bounds).addTo(map)

    map.fitBounds(bounds);
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