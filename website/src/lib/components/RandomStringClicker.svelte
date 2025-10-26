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