<script lang="ts">
    import type { Website } from "../../shared.svelte";
    let { website = undefined as Website|undefined, shown = $bindable(false) } = $props()
    import Dialog from "./Dialog.svelte";
</script>

<Dialog bind:shown={shown} title={website?.name}>
    {#snippet content()}
        <p>Something goes here</p>
    {/snippet}
</Dialog>