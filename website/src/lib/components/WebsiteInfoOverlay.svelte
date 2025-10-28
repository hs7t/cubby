<script lang="ts">
    import type { Website } from "../../shared.svelte";
    let { website = undefined as Website|undefined, shown = $bindable(false) } = $props()
    import Dialog from "./Dialog.svelte";
    import NavigateButton from "./NavigateButton.svelte";
</script>

<Dialog bind:shown={shown} title={website?.name}>
    {#snippet content()}
        <section>
            <h3>About</h3>
            <p>{website?.review}</p>
        </section>
        <section>
            <h3>Getting there</h3>
            <ol>
                {#each website?.directions as direction}
                    <li>{direction}</li>
                {/each}
            </ol>
        </section>
        <NavigateButton url={website?.url} />
    {/snippet}
</Dialog>