import websiteJSONURL from '/sites.json?url'

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

export const websites: Array<Website> = await (
    await fetch(websiteJSONURL)
).json()

export const uiState = $state({
    selectedWebsite: undefined as Website | undefined,
    websiteInfoOverlayShown: false,
})
