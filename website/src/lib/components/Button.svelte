<script>
    let { content = $bindable("click me!"), action, disabled = $bindable(false), id = "button-r", primary = false, addedClass = "" } = $props()
</script>

<button onclick={action} {disabled} {id} class={`${primary ? "primary" : "secondary"} ${addedClass}`}>
    {content}
</button>

<style>
    button {
        font-size: 1.2rem;
        padding: 0.4ch;
        font-weight: 600;
        text-transform: uppercase;
        background-color: var(--c-color-background-B);
        color: var(--c-color-primary);
        border: var(--c-border-generic);
        font-family: var(--c-font-family-primary);
        transition: all 100ms;
        cursor: pointer;
    }

    button:focus {
        outline: var(--c-border-attention);
        outline-offset: 3pt;
    }

    button:active {
        transform: scale(1.08);
    }

    button:hover {
        opacity: 0.9;
    }
</style>