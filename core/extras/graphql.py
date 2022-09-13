anime_search_query = """
query ($search: String) {
    Page{
        pageInfo {
            total
        }
        media (search: $search, type: ANIME) {
            id
        		idMal
            title {
                romaji
                english
                native
            }
        
        trailer {
            site
        }
        relations {
            nodes {
                title {
                    romaji
                }
                siteUrl
                type
            }
        }
            
        coverImage {
          extraLarge
          color
        }
        bannerImage
        type
        description
        meanScore
        episodes
        season
        popularity
        season
        type
        seasonYear
        startDate {
            day
            month
            year
        }
        endDate {
            day
            month
            year
        }
        status
        genres
        }
        }
        }
"""