# Telegram Channel Analytics: Growth and Reach

One row per public Telegram channel: subscribers and growth since your last run, median views, view rate, posting cadence, reactions and forward sources.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/telegram-channel-growth-analytics) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/telegram-channel-growth-analytics/)

**from $3.50 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

Telegram Channel Analytics: Growth and Reach turns a list of public Telegram channels into one analytics row per channel: subscribers, how many of them actually see a post (view rate), how often the channel posts, how people react, how much of it is forwarded from other channels, and how the audience changed since your last run.
It reads the public web preview of each channel, so there is no login, no API key and no Telegram account involved. Export the rows as JSON, CSV or Excel, call the Actor through the Apify API, or connect it to n8n, Make and AI agents through MCP.

## Quick start

1. Open [Telegram Channel Analytics: Growth and Reach on Apify Store](https://apify.com/datagrit/telegram-channel-growth-analytics) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "channels": [
    "telegram",
    "durov",
    "bloomberg",
    "rian_ru",
    "tass_agency",
    "nexta_live",
    "botnews",
    "tginfo",
    "contest",
    "designers",
    "habr_com",
    "proxy_tg"
  ],
  "postsPerChannel": 40,
  "maxItems": 50
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `channels` (required) | array | Public Telegram channels to analyse, one per line: usernames (telegram), with an at sign (@durov) or as links (https://t.me/bloomberg). Channels without a public web preview cannot be read and come back as status rows. |
| `postsPerChannel` | integer | How many of the latest posts feed the view, cadence, reaction and forward metrics. Telegram serves about 20 posts per request, so 40 posts cost two requests per channel. |
| `maxPostAgeDays` | integer | Ignore posts older than this many days, so rarely posting channels are not judged on years-old posts. 0 means no age limit; the latest post time is reported either way. |
| `minSubscribers` | integer | Skip channels with fewer subscribers than this. 0 disables the filter. Skipped channels are not charged and not recorded for growth tracking. |
| `maxSubscribers` | integer | Skip channels with more subscribers than this, for example to find mid-size channels. 0 disables the filter. |
| `maxItems` | integer | Stop after this many channel rows in total. Status rows do not count. |
| `proxyConfiguration` | object | Optional proxy. Leave disabled unless Telegram blocks the platform IP range; residential proxy raises the platform cost of the run. |

## Output

| Field | Type | Description |
|---|---|---|
| `channel` | string | Public username of the channel without the at sign, as Telegram writes it. Empty only on the status row of a run with no channel. |
| `channelUrl` | string | Link to the channel on t.me. |
| `title` | string | Display name of the channel. |
| `description` | string | Channel description from the public header; empty when the channel has none. |
| `verified` | boolean | True when Telegram shows the verified badge next to the channel name. |
| `subscribers` | integer | Subscriber count shown on the public page. Telegram rounds it above 10,000 (see subscribersApproximate). |
| `subscribersApproximate` | boolean | True when Telegram shows the count abbreviated (for example 9.38M), so the exact number is unknown; false for exact counts. |
| `photosTotal` | integer | Number of photos in the whole channel history as listed in the header counters; empty when the header does not list it. |
| `videosTotal` | integer | Number of videos in the whole channel history as listed in the header counters; empty when the header does not list it. |
| `linksTotal` | integer | Number of links in the whole channel history as listed in the header counters; empty when the header does not list it. |
| `postsAnalyzed` | integer | Number of recent posts the metrics below are computed from (limited by Posts per channel and Maximum post age). |
| `firstPostAt` | string | ISO 8601 time of the oldest post in the analysed sample. |
| `lastPostAt` | string | ISO 8601 time of the newest post on the channel, even when it falls outside the Maximum post age window. |
| `daysSinceLastPost` | number | Days between the run and the newest post; a quick inactivity check. |
| `postsPerDay` | number | Average posting cadence over the analysed sample (posts minus one, divided by the days they span); empty with fewer than two posts. |
| `viewsSamplePosts` | integer | Number of posts the view and reaction figures use: posts older than 24 hours when at least five exist, otherwise all posts with views. |
| `medianViews` | integer | Median views per post in the view sample; robust against one viral post. |
| `averageViews` | integer | Mean views per post in the view sample. |
| `maxViews` | integer | Highest view count in the view sample. |
| `viewRatePct` | number | Median views divided by current subscribers, in percent; the standard reach measure for ad buyers. Above 100 means posts are seen by far more people than subscribe, typical for rarely posting channels with viral history. |
| `postsWithReactions` | integer | Number of posts in the view sample that display a reactions bar; zero when the channel has reactions turned off. |
| `medianReactions` | number | Median number of emoji reactions per post (Stars reactions are excluded); empty when the channel shows no reactions. |
| `reactionsPer1kViews` | number | Total emoji reactions divided by views on the same posts, per 1,000 views. |
| `forwardedPosts` | integer | Number of analysed posts that were forwarded from another chat. |
| `forwardedSharePct` | number | Share of analysed posts that are forwards, in percent: high values mean the channel mostly redistributes other channels. |
| `topForwardSources` | array | Up to five channels this channel forwards from most, as objects with channel and posts. Sources that are private or users are not listed. |
| `mediaPostsSharePct` | number | Share of analysed posts that carry a photo, video, file, voice message or sticker. |
| `linkPostsSharePct` | number | Share of analysed posts that contain a link or a link preview. |
| `isFirstObservation` | boolean | True when your account has not read this channel before, so the growth columns are empty. |
| `observations` | integer | How many runs of your account have recorded this channel, including this one. |
| `previousCheckedAt` | string | ISO 8601 time of your previous run that included this channel. |
| `previousSubscribers` | integer | Subscriber count recorded at your previous run. |
| `subscribersChange` | integer | Current minus previous subscribers. Approximate when subscribersChangeApproximate is true, because Telegram abbreviates large counts. |
| `subscribersChangePct` | number | Subscribers change relative to the previous count, in percent. |
| `subscribersChangePerDay` | number | Subscribers change divided by the days since the previous check; empty when under one hour passed. |
| `subscribersChangeApproximate` | boolean | True when the current or the previous count was rounded by Telegram, so the change carries that rounding error. |
| `previousMedianViews` | integer | Median views recorded at your previous run. |
| `medianViewsChangePct` | number | Change of median views since the previous run, in percent; shows whether reach grows with the audience. |
| `found` | boolean | True for a channel row; false only for status rows that explain why a channel or the whole run returned no data. |
| `reason` | string | Present only on status rows: notFound, notAChannel, previewUnavailable, fetchFailed or filteredOut. |
| `message` | string | Present only on status rows: a sentence explaining the reason. |
| `sourceUrl` | string | Telegram web preview page the row was read from. |
| `scrapedAt` | string | ISO 8601 timestamp of extraction. |

Sample record:

```json
{
  "channel": "telegram",
  "channelUrl": "https://t.me/telegram",
  "title": "Telegram News",
  "description": "The official Telegram on Telegram. Much recursion. Very Telegram. Wow.",
  "verified": true,
  "subscribers": 9380000,
  "subscribersApproximate": true,
  "photosTotal": 16,
  "videosTotal": 228,
  "linksTotal": 378,
  "postsAnalyzed": 40,
  "firstPostAt": "2026-08-20T10:15:00.000Z",
  "lastPostAt": "2026-10-06T18:40:12.000Z",
  "daysSinceLastPost": 0.2,
  "postsPerDay": 1.4,
  "viewsSamplePosts": 38,
  "medianViews": 412000,
  "averageViews": 436800,
  "maxViews": 1200000,
  "viewRatePct": 4.39,
  "postsWithReactions": 38,
  "medianReactions": 5995,
  "reactionsPer1kViews": 18.3,
  "forwardedPosts": 4,
  "forwardedSharePct": 10,
  "topForwardSources": [
    {
      "channel": "khabib_nurmagomedov",
      "posts": 1
    }
  ],
  "mediaPostsSharePct": 47.4,
  "linkPostsSharePct": 10.5,
  "isFirstObservation": false,
  "observations": 5,
  "previousCheckedAt": "2026-10-05T07:00:00.000Z",
  "previousSubscribers": 9340000,
  "subscribersChange": 40000,
  "subscribersChangePct": 0.43,
  "subscribersChangePerDay": 20000,
  "subscribersChangeApproximate": true,
  "previousMedianViews": 398000,
  "medianViewsChangePct": 3.5,
  "found": true,
  "reason": "previewUnavailable",
  "message": "The channel exists but its owner disabled the public web preview.",
  "sourceUrl": "https://t.me/s/telegram",
  "scrapedAt": "2026-10-07T07:00:00.000Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~telegram-channel-growth-analytics/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"channels":["telegram","durov","bloomberg","rian_ru","tass_agency","nexta_live","botnews","tginfo","contest","designers","habr_com","proxy_tg"],"postsPerChannel":40,"maxItems":50}'
```

## FAQ

**Why is the view rate above 100%?**  
Views can exceed subscribers when posts are shared widely. If the sample contains old viral posts, set Maximum post age to 30 or 60 days for a current picture.

**Why does a channel come back without data?**  
The row says why: the username does not exist (`notFound`), belongs to a user, bot or group (`notAChannel`), or the channel owner disabled the public preview (`previewUnavailable`). Such rows are not charged.

**How fresh is the data?**  
Every run reads the preview live. Views of posts younger than 24 hours are still growing, so the median uses settled posts when at least five exist.

**Can I schedule runs?**  
Yes, use Apify schedules; the growth columns rely on repeated runs.

**Something looks wrong.**  
Open an issue with the input you used; layout changes at Telegram are fixed quickly.

## More from datagrit

- [Bilibili Anime Catalog, Rankings & Calendar](https://github.com/getdatagrit/bilibili-anime-series-tracker) - Bilibili anime, Chinese animation, film, documentary and TV series: filterable catalog, Top 100 rankings, release calendar and season details with ratings and follower counts.
- [Bluesky Community Finder: Starter Packs & Feeds](https://github.com/getdatagrit/bluesky-community-finder) - Find Bluesky starter packs, custom feeds and curated lists by topic, with join counts, feed likes and full member lists with follower counts.
- [Medium Publication Finder: Subscribers & Activity](https://github.com/getdatagrit/medium-publication-finder) - Find Medium publications by keyword and score each one: subscribers, posting cadence, claps per post, paywalled share and top authors.
- [Substack Newsletter Sponsorship Prospect Finder](https://github.com/getdatagrit/substack-sponsor-prospector) - Substack publications ranked for sponsorship: subscriber count, paid-tier size, plan prices, posting cadence and engagement per 1,000 subscribers.
- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/telegram-channel-growth-analytics). Examples are MIT licensed.
