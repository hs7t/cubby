<script lang="ts">
    import confetti from 'canvas-confetti'

    let heading = $state("cubby · website")
    const seasonHeadings = [
        "fall?? or autumn",
        "hot · chocolate",
        "pumpkin · website",
        "get some leaves!"
    ]

    const getRandomSeasonHeading = () => {
        return seasonHeadings[Math.floor(Math.random() * seasonHeadings.length)]
    }

    let scalar = 2;
    let leaf = confetti.shapeFromText({ text: '🍂', scalar });

    let count = 200;

    let defaults = {
        spread: 360,
        ticks: 60,
        gravity: 0,
        decay: 0.96,
        startVelocity: 20,
        shapes: [leaf],
        scalar,
        origin: { y: 2 }
    };

    const throwConfetti = (particleRatio: number, opts: object) => {
        confetti({
            ...defaults,
            ...opts,
            particleCount: Math.floor(count * particleRatio)
        });
    }

    const handleHeadingButtonClick = () => {
        throwConfetti(0.25, {
            spread: 26,
            startVelocity: 55,
        });
        throwConfetti(0.2, {
            spread: 60,
        });
        throwConfetti(0.35, {
            spread: 100,
            decay: 0.91,
            scalar: 0.8
        });
        throwConfetti(0.1, {
            spread: 120,
            startVelocity: 25,
            decay: 0.92,
            scalar: 1.2
        });
        throwConfetti(0.1, {
            spread: 120,
            startVelocity: 45,
        });

        heading = getRandomSeasonHeading()
    }
</script>

<header>
    <h1>{heading}</h1>
    <button id="leafButton" onclick={handleHeadingButtonClick}>🍂</button>
</header>

<style>
    header {
        width: 100%;
        display: flex;
        flex-direction: row;
        gap: 1em;
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

    #leafButton {
        padding: 1ch;
        border: var(--c-border-generic);
        background-color: var(--c-color-background-B);
        user-select: none;
        transition: all 100ms;
    }

    #leafButton:hover {
        transform: scale(0.8) rotate(-5deg);
    }

    #leafButton:focus {
        outline: var(--c-border-attention);
        outline-offset: 3pt;
    }

    #leafButton:active {
        transform: scale(2) rotate(5deg);
    }
</style>