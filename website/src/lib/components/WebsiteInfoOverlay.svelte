<script lang="ts">
    import type { Website } from "../../shared.svelte";
    let { website = undefined as Website|undefined, shown = $bindable(false) } = $props()
    import Dialog from "./Dialog.svelte";
</script>

<Dialog bind:shown={shown}>
    {#snippet content()}
        <h2>{website?.name}</h2>
    {/snippet}
</Dialog>