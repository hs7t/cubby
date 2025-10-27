<script lang="ts">
    import type { Website } from "../../shared.svelte";
    let { website = undefined as Website|undefined } = $props()
    import Dialog from "./Dialog.svelte";
</script>

<Dialog>
    {#snippet content()}
        <h2>{website?.name}</h2>
    {/snippet}
</Dialog>