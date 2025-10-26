
<div class="navigator">
    <div class="item">
        <div class="number">
            <p>1</p>
        </div>
        <div class="info">
            <p class="site-name">Ali's Website</p>
            <p class="site-address">12 Raspberry Way, HUK</p>
        </div>
    </div>
</div>

<style>
    .navigator .item {
        display: flex;
        flex-direction: row;

        padding: 0.5rem;

        background-color: var(--c-color-background-B);
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