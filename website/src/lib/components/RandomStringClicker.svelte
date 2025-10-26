<script lang="ts">
    let { strings = [] as Array<string> } = $props()
    
    let currentString = $state("")
    const randomString = () => {
        const randomIndex = Math.floor(Math.random() * strings.length)
        return strings[randomIndex]
    }
    const updateString = () => {
        currentString = randomString()
    }
    updateString()
</script>

<button onclick={updateString}>
    {currentString}
</button>

<style>
    button {
        align-self: center;
        background-color: var(--c-color-background-B);
        border-radius: 100pt;
        border: none;
        user-select: none;
        transition: all 100ms;

        font-family: var(--c-font-family-display);
        font-size: var(--c-font-size-B);
        text-transform: uppercase;
        color: inherit;
    }

    button:active {
        transform: scale(0.9) rotate(5deg);
    }
</style>