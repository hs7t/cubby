<script>
    import { websites } from "../../shared.svelte";
</script>


<section class="navigation">
    <div class="navigator">
        {#each websites as website}
            <div class="item">
                <div class="number">
                    <p>{websites.indexOf(website)}</p>
                </div>
                <div class="info">
                    <p class="site-name">{website.name}</p>
                    <p class="site-address">{website.address}</p>
                </div>
            </div>
        {/each}
    </div>
</section>

<style>
    .navigation {
        display: flex;
        flex-direction: column;
    }

    .navigator {
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        flex-grow: 1;
        gap: 0.2em;
    }

    .navigator .item {
        display: flex;
        flex-direction: row;

        padding: 0.5rem;

        background-color: var(--c-color-background-B);
        border: var(--c-border-generic);
    }

    .navigator .item p {
        text-transform: uppercase;
        font-weight: 500;
    }

    .navigator .item .info {
        flex-grow: 2;
    }

    .navigator .item .info p {
        width: 100%;
        text-align: right;
    }
</style>