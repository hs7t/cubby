export type Marker = {
    coordinates: Array<number>
    title: string
    action: Function
    id: string
}

export type Website = {
    cubbyId: string
    name: string
    url: string
    address: string
    mapCoordinates: Array<number>
    review: string
    directions: Array<string>
}

const shuffle = (array: Array<any>) => {
    return array.sort(() => Math.random() - 0.5)
}

export const websites = undefined as Array<Website>
console.log(websites)

export const uiState = $state({
    selectedWebsite: undefined as Website | undefined,
    websiteInfoOverlayShown: false,
})
