<script lang="ts">
  import Button from "./Button.svelte";

    let { content, title = "Dialog", shown = $bindable() } = $props()
    let dialogReference: HTMLDialogElement
    
    $effect(() => {
        if (shown) {
            dialogReference.showModal()
        } else {
            dialogReference.close()
        }
    })
</script>

<dialog class="dialog" bind:this={dialogReference} onclose={() => shown = false} closedby="any">
    <nav>
        <h2>{title}</h2>
        <Button id="close-button" content="Close" action={() => { shown = false }} />
    </nav>
    {@render content()}
</dialog>

<style>
    .dialog {
        width: clamp(280px, 100%, 560px);
        display: flex;
        flex-direction: column;
        gap: 1rem;
        align-items: flex-start;

        color: var(--c-color-primary);
        font-size: 1.5rem;
        border: var(--c-border-generic);
        background-color: var(--c-color-background-C);

        animation: 100ms dialogEnter;
        animation-timing-function: cubic-bezier(0.075, 0.82, 0.165, 1);
        transition-behavior: allow-discrete;
        transition: all 50ms;

        align-self: center;
        justify-self: center;
    }

    .dialog:focus {
        outline: var(--c-border-attention);
        outline-offset: 3pt;
    }

    @keyframes dialogEnter {
        0% {
            transform: scale(0.98);
            opacity: 0.7;
        }
        100% {
            transform: none;
            opacity: 1;
        }
    }

    .dialog::backdrop {
        opacity: 0;
    }

    .dialog nav {
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }

    :global(.dialog h2, .dialog h3, .dialog p) {
        font-size: inherit;
    }

    :global(.dialog h2, .dialog h3) {
        text-transform: uppercase;
        width: 100%;
    }

    :global(.dialog h2) {
        text-align: center;
    }

    :global(#close-button) {
        align-self: flex-end;
    }

    :global(ol) {
        max-width: 100%;
        list-style-type: decimal;
    }

    .dialog:not([open]) {
        display: none;
        transition: all;
    }
</style>