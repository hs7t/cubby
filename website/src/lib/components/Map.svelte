<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import L, { icon } from "leaflet"
    import LargeMapImg from '../../assets/Large Map.svg'
    import type { Marker } from "../../shared.svelte";

    let { markers = undefined as undefined|Array<Marker>, addedMarkers = $bindable({}) as Record<string, L.Marker> } = $props()

    let mapElement
    let map: L.Map

    onMount(async () => {
        map = L.map('map', {
            crs: L.CRS.Simple,
            minZoom: -2,
            attributionControl: false,
        })
        let bounds: L.LatLngBoundsExpression = [[0, 0], [1000, 1000]]
        let image = L.imageOverlay(LargeMapImg, bounds).addTo(map)

        if (markers != undefined) {
            let defaultMarkerNumberIcon: L.DivIconOptions = {
                className: "markerNumberIcon",
                html: "<div>1</div>",
                iconSize: [20, 20],
                iconAnchor: [10, 10], // half of width + height, for some reason
            }

            for (let marker of markers) {
                let markerNumberIcon = L.divIcon({ ...defaultMarkerNumberIcon, html: `<div>${Object.keys(addedMarkers).length}</div>` })

                addedMarkers[marker.id] = L.marker(marker.coordinates as L.LatLngTuple, { icon: markerNumberIcon }).addTo(map)
                addedMarkers[marker.id].bindPopup(marker.title)
                addedMarkers[marker.id].on('click', marker.action as L.LeafletMouseEventHandlerFn)
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

    :global(.markerNumberIcon) {
        display: flex;
        align-items: center;
        justify-content: center;

        background-color: var(--c-color-background-C);
        border: 1.5pt solid var(--c-color-primary);
        border-radius: 100pt;
        font-weight: 600;
        font-size: 0.75rem;
        color: var(--c-color-primary);
    }
</style>