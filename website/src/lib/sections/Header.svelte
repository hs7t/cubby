<script lang="ts">
    import confetti from 'canvas-confetti'
    var scalar = 2;
    var leaf = confetti.shapeFromText({ text: '🍂', scalar });

    var count = 200;

    var defaults = {
        spread: 360,
        ticks: 60,
        gravity: 0,
        decay: 0.96,
        startVelocity: 20,
        shapes: [leaf],
        scalar,
        origin: { y: 2 }
    };

    function fire(particleRatio: number, opts: object) {
        confetti({
            ...defaults,
            ...opts,
            particleCount: Math.floor(count * particleRatio)
        });
    }

    const handleHeadingClick = () => {
    fire(0.25, {
    spread: 26,
    startVelocity: 55,
    });
    fire(0.2, {
    spread: 60,
    });
    fire(0.35, {
    spread: 100,
    decay: 0.91,
    scalar: 0.8
    });
    fire(0.1, {
    spread: 120,
    startVelocity: 25,
    decay: 0.92,
    scalar: 1.2
    });
    fire(0.1, {
    spread: 120,
    startVelocity: 45,
    });    }
</script>

<header>
    <a onclick={handleHeadingClick}>
        <h1>cubby.website</h1>
    </a>
</header>

<style>
    header {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        padding-bottom: 0.5rem;
        border-bottom: var(--c-border-generic);
    }

    h1 {
        font-size: var(--c-font-size-AAA);
        font-family: var(--c-font-family-display);
        font-weight: 400;
    }
</style>