<script>
    import { uiState, websites } from "../../shared.svelte";
</script>


<section class="navigation">
    <div class="navigator">
        {#each websites as website}
            <button class="item" onclick={() => {
                uiState.selectedWebsite = website
                uiState.websiteInfoOverlayShown = true
            }}>
                <div class="number">
                    <p>{websites.indexOf(website)}</p>
                </div>
                <div class="info">
                    <p class="site-name">{website.name}</p>
                    <p class="site-address">{website.address}</p>
                </div>
            </button>
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
        max-height: 100%;
        overflow-y: scroll;
        flex-grow: 1;
        gap: 0.2em;
    }

    .navigator .item {
        all: unset;

        display: flex;
        flex-direction: row;

        padding: 0.5rem;

        background-color: var(--c-color-background-B);
        border: var(--c-border-generic);
        cursor: pointer;
        transition: all 200ms;
    }

    .navigator .item:focus {
        outline: var(--c-border-attention);
        outline-offset: 1pt;
        animation: 200ms navigationFocusing;
    }

    .navigator .item:hover {
        transform: rotate(-1deg) scale(0.9);
    }

    .navigator .item:active {
        transform: rotate(5deg) scale(0.9);
    }

    @keyframes navigationFocusing {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(0.98);
        }
        100% {
            transform: scale(1);
        }
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