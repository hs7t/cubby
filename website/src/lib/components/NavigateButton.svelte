<script>
    let { content = "Navigate", url, disabled = $bindable(false), id = "button-navigate" } = $props()
</script>

<div class="navigateButtonContainer">
    <button onclick={() => window.open(url, "_blank", 'location=yes,height=570,width=520,scrollbars=yes,status=yes')} {disabled} {id}>
        {content}
    </button>
    <small>(will take you to {url})</small>
</div>

<style>
    .navigateButtonContainer {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-items: center;
        align-self: center;
        gap: 0.5rem;
    }

    small {
        font-size: 0.8rem;
    }

    button {
        font-size: 1.5rem;
        padding: 0.5ch;
        font-weight: 600;
        text-transform: uppercase;
        background-color: var(--c-color-background-B);
        color: var(--c-color-primary);
        border: var(--c-border-generic);
        font-family: var(--c-font-family-primary);
        transition: all 100ms;
    }

    button:focus {
        outline: var(--c-border-attention);
        outline-offset: 3pt;
    }

    button:active {
        transform: translateY(-0.3rem);
    }

    button:hover {
        transform: scale(1.08);
        opacity: 0.9;
    }
</style>