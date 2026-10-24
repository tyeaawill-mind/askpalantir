# id, src(slug), true statement, false statement, explanation (the true fact), evidence strings (must appear in src page text)
F = []
def add(i, src, t, f, ex, ev): F.append(dict(id=i, src=src, t=t, f=f, ex=ex, ev=ev))

# ---- Company & products
add("founded", "who-founded-palantir",
    "Palantir was founded in 2003.",
    "Palantir was founded in 2010.",
    "Palantir was co-founded in 2003 by Peter Thiel, Alex Karp, and a founding team.",
    ["founded in 2003"])
add("directlist", "who-founded-palantir",
    "Palantir went public through a direct listing on September 30, 2020.",
    "Palantir went public through a traditional underwritten IPO in 2020.",
    "Palantir listed via a direct listing on September 30, 2020, not a traditional IPO.",
    ["direct listing on the new york stock exchange on september 30, 2020"])
add("paypal", "who-founded-palantir",
    "Palantir co-founder Peter Thiel previously co-founded PayPal.",
    "Palantir co-founder Peter Thiel previously co-founded Uber.",
    "Peter Thiel is best known as a co-founder of PayPal.",
    ["co-founder of paypal"])
add("intaqtel", "who-founded-palantir",
    "One of Palantir's earliest funders was In-Q-Tel, the venture capital arm of the CIA.",
    "One of Palantir's earliest funders was In-Q-Tel, the venture capital arm of the NSA.",
    "In-Q-Tel is the venture capital arm of the CIA, and it was one of Palantir's earliest sources of funding.",
    ["venture capital arm of the cia"])
add("karpphd", "who-founded-palantir",
    "CEO Alex Karp holds a PhD in philosophy.",
    "CEO Alex Karp holds a PhD in computer science.",
    "Alex Karp holds a PhD in philosophy, not a computer science or engineering degree.",
    ["phd in philosophy"])
add("tolkien", "what-does-the-name-palantir-mean",
    "The name 'Palantir' comes from Tolkien's Lord of the Rings, where a palantir is a seeing-stone.",
    "The name 'Palantir' comes from Greek mythology.",
    "The name comes from J.R.R. Tolkien's The Lord of the Rings, where a palantir is a seeing-stone.",
    ["tolkien", "seeing-stone"])
add("nasdaq", "how-to-buy-palantir-stock",
    "Palantir's stock trades on the Nasdaq under the ticker PLTR.",
    "Palantir's stock trades on the NYSE under the ticker PLTR.",
    "PLTR trades on the Nasdaq.",
    ["ticker symbol pltr on the nasdaq"])
add("move2024", "how-to-buy-palantir-stock",
    "Palantir moved its stock listing from the NYSE to Nasdaq in November 2024.",
    "Palantir moved its stock listing from Nasdaq to the NYSE in November 2024.",
    "The company moved its listing from the NYSE to Nasdaq in November 2024.",
    ["november 2024"])
add("gothamgov", "what-is-palantir-gotham",
    "Gotham is Palantir's platform for government, defense, and intelligence work; Foundry is its commercial platform.",
    "Foundry is Palantir's platform for government, defense, and intelligence work; Gotham is its commercial platform.",
    "Gotham is the original government, defense, and intelligence platform. Foundry is the commercial counterpart.",
    ["government, defense, and intelligence"])
add("connectors", "what-is-palantir-foundry",
    "Foundry connects to an organization's existing systems through more than 200 built-in connectors.",
    "Foundry connects to an organization's existing systems through fewer than 20 built-in connectors.",
    "Foundry offers more than 200 built-in connectors to existing systems.",
    ["more than 200 built-in connectors"])
add("ontologyproduct", "what-is-the-palantir-ontology",
    "The Palantir Ontology is not a separate product; it is built into both Foundry and Gotham.",
    "The Palantir Ontology is a separate product sold only to government customers.",
    "The Ontology isn't a separate product. It's built into both Foundry and Gotham.",
    ["isn't a separate product"])
add("apolloairgap", "what-is-palantir-apollo",
    "Apollo is Palantir's deployment platform, able to push software updates even into air-gapped networks.",
    "Apollo is Palantir's customer-support chatbot for answering billing questions.",
    "Apollo continuously delivers updates across cloud, on-premises, and fully disconnected air-gapped environments.",
    ["air-gapped"])
add("hubspoke", "what-is-palantir-apollo",
    "Apollo's architecture is built around Hubs and Spokes.",
    "Apollo's architecture is built around Towers and Bridges.",
    "Apollo uses Hub environments that issue update plans and Spoke environments that execute them.",
    ["hub environments", "spoke environments"])
add("fedstart", "what-is-palantir-apollo",
    "FedStart lets other software vendors deploy their products inside Palantir's accredited FedRAMP environments.",
    "FedStart is Palantir's employee stock purchase program.",
    "FedStart lets other vendors deploy inside Palantir's already-accredited FedRAMP and Impact Level environments.",
    ["deploy their own products inside palantir"])
add("aip2023", "what-is-palantir-aip",
    "AIP, Palantir's Artificial Intelligence Platform, launched in 2023.",
    "AIP, Palantir's Artificial Intelligence Platform, launched in 2016.",
    "AIP is the newest of Palantir's four core products, launched in 2023.",
    ["2023 launch"])
add("bootcamp", "what-is-a-palantir-aip-bootcamp",
    "Palantir AIP Bootcamps typically run one to five days.",
    "Palantir AIP Bootcamps typically run six months.",
    "Bootcamps are short, hands-on sessions that typically run one to five days.",
    ["one to five days"])
add("fde", "what-is-a-forward-deployed-engineer",
    "A Forward Deployed Engineer combines software engineering with client-facing work for a specific customer.",
    "A Forward Deployed Engineer works only on Palantir's internal codebase and never interacts with customers.",
    "Forward Deployed Engineers combine engineering with direct, client-facing work.",
    ["client-facing"])
add("acquire", "how-does-palantir-make-money",
    "Palantir describes its customer relationships as moving through three phases: Acquire, Expand, and Scale.",
    "Palantir describes its customer relationships as moving through four phases: Pilot, Pause, Pivot, and Profit.",
    "The three phases are Acquire, Expand, and Scale.",
    ["acquire, expand, scale"])
add("subs", "how-does-palantir-make-money",
    "Palantir makes money primarily by selling software subscriptions.",
    "Palantir makes money primarily from one-time hardware sales.",
    "Palantir's revenue comes primarily from software subscriptions, not data sales or one-off consulting.",
    ["selling software subscriptions"])
add("margins", "how-does-palantir-make-money",
    "Palantir's gross margins have been reported above 80%, far higher than a typical consulting firm.",
    "Palantir's gross margins have been reported around 30-40%, typical of a consulting firm.",
    "Palantir's gross margins have run consistently above 80%, closer to software than consulting.",
    ["above 80%"])
add("rio2021", "palantir-rio-tinto-partnership",
    "Palantir and Rio Tinto signed a multi-year Foundry agreement in January 2021.",
    "Palantir and Rio Tinto signed a multi-year Foundry agreement in January 2015.",
    "The Foundry enterprise agreement was signed in January 2021.",
    ["january 2021"])
add("rio2024", "palantir-rio-tinto-partnership",
    "In 2024, Palantir and Rio Tinto extended their agreement by four years, adding access to AIP.",
    "In 2024, Palantir and Rio Tinto ended their agreement after a dispute over AIP.",
    "In November 2024 the agreement was renewed for an additional four years, adding AIP.",
    ["additional four years"])
# ---- Financial statements and metrics
add("auditor", "how-to-read-palantirs-financial-statements",
    "Palantir's independent auditor is Ernst & Young LLP.",
    "Palantir's independent auditor is Deloitte.",
    "Palantir's independent auditor is Ernst & Young LLP, based in San Jose, California.",
    ["ernst & young llp"])
add("tenq", "how-to-read-palantirs-financial-statements",
    "A 10-K is an audited annual report, while a 10-Q is an unaudited quarterly update.",
    "A 10-Q is an audited annual report, while a 10-K is an unaudited quarterly update.",
    "The 10-K is the audited annual report; the 10-Q is an unaudited quarterly update.",
    ["unaudited quarterly update"])
add("cam", "how-to-read-palantirs-financial-statements",
    "In Palantir's FY2023 10-K, the auditor flagged revenue recognition on on-premises software contracts as a critical audit matter.",
    "In Palantir's FY2023 10-K, the auditor flagged the company's cash balance as a critical audit matter.",
    "The critical audit matter concerned revenue recognition around on-premises software contracts, a judgment-heavy area common across software companies.",
    ["revenue recognition around the company's on-premises software contracts"])
add("fyend", "how-does-palantir-report-earnings",
    "Palantir's fiscal year ends on December 31.",
    "Palantir's fiscal year ends on June 30.",
    "Palantir uses a standard calendar-year fiscal year, ending December 31.",
    ["ending december 31"])
add("eightk", "how-does-palantir-report-earnings",
    "Palantir's quarterly results are first announced in an 8-K filing with an attached press release.",
    "Palantir's quarterly results are first announced only in the annual 10-K.",
    "Results first appear in an 8-K with a press release, followed by the earnings call, investor presentation, and the 10-Q or 10-K.",
    ["8-k filing with an attached press release"])
add("rev2021", "what-has-palantirs-revenue-growth-looked-like",
    "Palantir's FY2021 revenue was about $1.54 billion.",
    "Palantir's FY2021 revenue was about $4.5 billion.",
    "Full-year revenue was $1.54 billion in FY2021, up 41% year over year.",
    ["$1.54 billion in fy2021"])
add("rev2025", "what-has-palantirs-revenue-growth-looked-like",
    "Palantir's full-year 2025 revenue was roughly $4.47 billion.",
    "Palantir's full-year 2025 revenue was roughly $9 billion.",
    "Government plus commercial segments totaled roughly $4.47 billion in FY2025.",
    ["$4.47 billion"])
add("q2growth", "what-has-palantirs-revenue-growth-looked-like",
    "Palantir's Q2 2026 total revenue grew 93% year over year.",
    "Palantir's Q2 2026 total revenue grew 9% year over year.",
    "Palantir's own Q2 2026 release reported total revenue growth of 93% year over year.",
    ["93% year-over-year"])
add("q2uscomm", "what-has-palantirs-revenue-growth-looked-like",
    "In Q2 2026, Palantir's U.S. commercial revenue grew 149% year over year.",
    "In Q2 2026, Palantir's U.S. commercial revenue grew 14% year over year.",
    "U.S. commercial revenue was up 149% year over year to $764 million.",
    ["149% year-over-year"])
add("guidance", "what-has-palantirs-revenue-growth-looked-like",
    "After its Q2 2026 report, Palantir raised full-year 2026 revenue guidance to roughly $8.15 billion.",
    "After its Q2 2026 report, Palantir cut full-year 2026 revenue guidance to roughly $2.15 billion.",
    "Palantir raised full-year 2026 revenue guidance to $8.15-8.16 billion.",
    ["$8.15"])
add("ruleof40", "what-are-palantirs-key-financial-metrics",
    "Palantir reported a Rule of 40 score of 155% in Q2 2026.",
    "Palantir reported a Rule of 40 score of 15% in Q2 2026.",
    "Palantir reported a Rule of 40 score of 155% in Q2 2026.",
    ["155% in q2 2026"])
add("ruledef", "what-are-palantirs-key-financial-metrics",
    "The Rule of 40 adds a company's revenue growth rate to its profit margin.",
    "The Rule of 40 caps stock-based compensation at 40% of revenue.",
    "The Rule of 40 adds revenue growth to profit margin. Above 40% is generally considered healthy.",
    ["adds a company's year-over-year revenue growth rate to its profit margin"])
add("fcf", "what-are-palantirs-key-financial-metrics",
    "Palantir's adjusted free cash flow in Q2 2026 was about $1.22 billion.",
    "Palantir's adjusted free cash flow in Q2 2026 was about $122 million.",
    "Adjusted free cash flow was $1.220 billion in Q2 2026, a 63% margin.",
    ["$1.220 billion"])
add("cash", "what-are-palantirs-key-financial-metrics",
    "Palantir held $9.2 billion in cash and short-term securities as of Q2 2026.",
    "Palantir held $920 million in cash and short-term securities as of Q2 2026.",
    "Cash and short-term U.S. Treasuries reached $9.2 billion by Q2 2026.",
    ["$9.2 billion"])
add("ni871", "what-are-palantirs-key-financial-metrics",
    "Palantir reported GAAP net income of $871 million in Q1 2026.",
    "Palantir reported a GAAP net loss of $871 million in Q1 2026.",
    "Q1 2026 GAAP net income was $871 million.",
    ["$871 million"])
# ---- Comparisons, markets, IPOs
add("sp500", "palantir-vs-spacex-ipo-comparison",
    "Palantir was added to the S&P 500 in September 2025.",
    "Palantir was added to the S&P 500 the week after its 2020 listing.",
    "Palantir joined the S&P 500 in September 2025, roughly five years after its direct listing.",
    ["september 2025"])
add("spacexipo", "palantir-vs-spacex",
    "SpaceX priced its IPO at $135 per share on June 12, 2026.",
    "SpaceX priced its IPO at $35 per share on June 12, 2026.",
    "SpaceX priced at $135 per share on June 12, 2026.",
    ["$135 per share on june 12, 2026"])
add("spcx", "palantir-vs-spacex",
    "SpaceX trades on the Nasdaq under the ticker SPCX.",
    "SpaceX trades on the NYSE under the ticker SPX.",
    "SpaceX listed on the Nasdaq under the ticker SPCX.",
    ["spcx"])
add("muskvote", "palantir-vs-spacex-ipo-comparison",
    "After its IPO, Elon Musk retained roughly 82-85% of SpaceX's voting power.",
    "After its IPO, Elon Musk retained roughly 8% of SpaceX's voting power.",
    "Musk retained roughly 82-85% of voting power after the IPO.",
    ["82-85% of voting power"])
add("bigipo", "palantir-vs-spacex-ipo-comparison",
    "SpaceX's 2026 IPO was reported as the largest IPO in history by capital raised.",
    "SpaceX's 2026 IPO raised less than Palantir's 2020 direct listing.",
    "SpaceX's 2026 IPO was reported as the largest in history by capital raised.",
    ["largest ipo in history by capital raised"])
add("spacexrev", "palantir-vs-spacex",
    "SpaceX reported roughly $18.6-18.7 billion in revenue for 2025.",
    "SpaceX reported roughly $186 million in revenue for 2025.",
    "SpaceX's 2025 revenue was roughly $18.6-18.7 billion.",
    ["$18.6-18.7 billion"])
add("starlink", "palantir-vs-spacex",
    "Starlink generated about 61% of SpaceX's 2025 revenue.",
    "Starlink generated about 6% of SpaceX's 2025 revenue.",
    "Starlink produced $11.4 billion, 61% of SpaceX's total 2025 revenue.",
    ["61% of total revenue"])
add("spacexloss", "palantir-vs-spacex",
    "SpaceX posted a GAAP net loss of nearly $5 billion for 2025.",
    "SpaceX posted a GAAP net profit of nearly $5 billion for 2025.",
    "SpaceX posted a GAAP net loss of nearly $5 billion for full-year 2025, even though Starlink was profitable on its own.",
    ["net loss of nearly $5 billion"])
add("spacextam", "palantir-vs-spacex-tam-comparison",
    "SpaceX reportedly cited a total addressable market of $28.5 trillion around its IPO.",
    "SpaceX reportedly cited a total addressable market of $28.5 million around its IPO.",
    "The reported SpaceX figure was $28.5 trillion, and analysts have questioned how it was built.",
    ["$28.5 trillion"])
add("pltrtam", "palantir-vs-spacex-tam-comparison",
    "At its 2020 listing, Palantir estimated its addressable market at roughly $119 billion.",
    "At its 2020 listing, Palantir estimated its addressable market at roughly $1.19 trillion.",
    "The 2020 estimate was roughly $119 billion, split $56 billion commercial and $63 billion government.",
    ["$119 billion"])
add("sap2025", "palantir-vs-sap",
    "SAP and Palantir announced an engineering partnership in May 2025.",
    "SAP and Palantir announced an engineering partnership in May 2015.",
    "The partnership was announced in May 2025.",
    ["may 2025"])
add("dbxzero", "palantir-vs-databricks",
    "Palantir and Databricks announced a strategic partnership enabling zero-copy data integration.",
    "Palantir announced it was acquiring Databricks to enable zero-copy data integration.",
    "The two companies partnered on zero-copy data integration. They are partners as well as frequently compared.",
    ["zero-copy"])
add("lakehouse", "palantir-vs-databricks",
    "Databricks' core architecture is known as the 'Lakehouse'.",
    "Databricks' core architecture is known as the 'Ontology'.",
    "Databricks centers on its Lakehouse architecture. The Ontology is Palantir's concept.",
    ["lakehouse"])
add("snowprice", "palantir-vs-snowflake",
    "Snowflake's pricing has traditionally been usage-based, while Palantir generally sells platform subscriptions.",
    "Palantir's pricing has traditionally been usage-based, while Snowflake generally sells platform subscriptions.",
    "Snowflake charges for compute and storage consumed; Palantir generally sells platform subscriptions with implementation support.",
    ["usage-based"])
add("nvidia50", "palantir-vs-nvidia",
    "In Q1 2026, Nvidia's quarterly revenue was more than 50 times Palantir's.",
    "In Q1 2026, Nvidia's quarterly revenue was about the same as Palantir's.",
    "Nvidia's $81.6 billion quarter was more than 50 times Palantir's $1.6 billion.",
    ["more than 50 times palantir's"])
add("growth85", "palantir-vs-nvidia",
    "In Q1 2026, Palantir's revenue growth of 85% year over year roughly matched Nvidia's.",
    "In Q1 2026, Palantir's revenue was shrinking while Nvidia's grew 85%.",
    "Both grew about 85% year over year that quarter despite the huge scale gap.",
    ["grew 85% year-over-year"])
add("luckey", "palantir-vs-anduril",
    "Anduril was founded by Palmer Luckey.",
    "Anduril was founded by Alex Karp.",
    "Anduril was founded by Palmer Luckey after he left Meta.",
    ["palmer luckey"])
add("consortium", "palantir-vs-anduril",
    "Palantir and Anduril formed a consortium in December 2024.",
    "Palantir and Anduril merged in December 2024.",
    "They formed a consortium combining Palantir's data fusion with Anduril's Lattice and edge hardware.",
    ["december 2024"])
add("monopoly", "is-palantir-a-monopoly",
    "No formal antitrust finding has determined that Palantir holds an illegal monopoly.",
    "A U.S. court has ruled that Palantir holds an illegal monopoly.",
    "No formal antitrust finding exists. 'Monopoly' is mostly informal commentary about competitive position.",
    ["no formal antitrust finding"])
add("tsmc", "palantirs-competitive-vulnerabilities",
    "TSMC's dominant vulnerability is geopolitical, centered on Taiwan.",
    "TSMC's dominant vulnerability is heavy dependence on a single U.S. federal agency.",
    "TSMC sits at the center of U.S.-China tensions over Taiwan, a risk Palantir doesn't share.",
    ["tsmc's dominant vulnerability is geopolitical"])
# ---- Government and controversy (documented facts and attributed statements only)
add("armyreadiness", "what-government-contracts-does-palantir-hold",
    "Palantir has said its software helps track the readiness of more than a million U.S. Army personnel.",
    "Palantir has said its software tracks the readiness of fewer than a thousand U.S. Army personnel.",
    "Palantir has stated its software helps track readiness for more than a million U.S. Army personnel.",
    ["more than a million u.s. army personnel"])
add("govshare", "what-government-contracts-does-palantir-hold",
    "Government revenue was roughly 55% of Palantir's total revenue as of mid-2025.",
    "Government revenue was roughly 5% of Palantir's total revenue as of mid-2025.",
    "Government made up roughly 55% of total revenue as of mid-2025, per the company's own reporting.",
    ["roughly 55% of palantir's total revenue"])
add("ice2011", "does-palantir-work-with-ice",
    "Palantir's work with ICE dates back to 2011.",
    "Palantir's work with ICE began in 2021.",
    "Palantir has worked with ICE since 2011.",
    ["since 2011"])
add("immos", "does-palantir-work-with-ice",
    "An ImmigrationOS contract worth $30 million was awarded to Palantir in April 2025.",
    "An ImmigrationOS contract worth $30 billion was awarded to Palantir in April 2025.",
    "The ImmigrationOS contract was $30 million, awarded in April 2025.",
    ["$30 million contract awarded in april 2025"])
add("irs2018", "what-is-palantirs-irs-contract",
    "The IRS Criminal Investigation division has used a Palantir platform called Lead and Case Analytics since 2018.",
    "The IRS Criminal Investigation division has used a Palantir platform called Lead and Case Analytics since 2008.",
    "The IRS has used Lead and Case Analytics, built on Gotham and Foundry, since 2018.",
    ["lead and case analytics"])
add("irs130", "what-is-palantirs-irs-contract",
    "Public records show the IRS has paid Palantir over $130 million since 2018.",
    "Public records show the IRS has paid Palantir over $13 million since 2018.",
    "Reported payments exceed $130 million since 2018, per records obtained by American Oversight.",
    ["over $130 million"])
add("nhs330", "palantir-nhs-contract-controversy",
    "Palantir's NHS Federated Data Platform contract is worth up to 330 million pounds over seven years.",
    "Palantir's NHS Federated Data Platform contract is worth up to 330 billion pounds over seven years.",
    "The contract is worth up to \u00a3330 million over seven years.",
    ["\u00a3330 million over seven years"])
add("nhs2020", "palantir-nhs-contract-controversy",
    "Palantir's NHS involvement began in March 2020 under emergency COVID-19 procurement rules.",
    "Palantir's NHS involvement began in 2017 after a full competitive tender.",
    "It began in March 2020 without a competitive tender, under emergency COVID-19 rules.",
    ["march 2020"])
add("nhs2023", "palantir-nhs-contract-controversy",
    "The NHS Federated Data Platform contract was awarded in November 2023.",
    "The NHS Federated Data Platform contract was awarded in November 2019.",
    "The Palantir-led consortium was awarded the platform contract in November 2023.",
    ["november 2023"])
add("doge", "what-was-palantirs-role-in-doge",
    "DOGE was established by executive order on January 20, 2025, by renaming the U.S. Digital Service.",
    "DOGE was established by an act of Congress in 2019.",
    "DOGE was created by executive order on January 20, 2025, by renaming the existing U.S. Digital Service.",
    ["january 20, 2025"])
add("prism", "does-palantir-spy-on-americans",
    "Palantir has its own unrelated product called Prism, used for financial data analysis, separate from the NSA program.",
    "Palantir's Prism product is the software that runs the NSA's PRISM program.",
    "In 2013 Palantir pointed out that its own Prism is an unrelated financial-analysis tool used by banks and hedge funds.",
    ["financial data analysis by banks and hedge funds"])
add("xkeyscore", "does-palantir-spy-on-americans",
    "According to Palantir's own blog response, it has never held a direct NSA contract and played no role in building XKEYSCORE.",
    "According to Palantir's own blog response, it helped build the NSA's XKEYSCORE tool.",
    "That is Palantir's stated position. The Intercept's reporting disputes it, as our page on the topic explains.",
    ["never held a direct nsa contract"])
add("intercept", "does-palantir-spy-on-americans",
    "The Intercept's 2017 reporting on Palantir and XKEYSCORE was based on documents provided by Edward Snowden.",
    "The Intercept's 2017 reporting on Palantir and XKEYSCORE was based on a leaked Palantir internal memo.",
    "The 2017 reporting was based on documents provided by Edward Snowden.",
    ["based on documents provided by edward snowden"])
add("karpquote", "is-palantir-ethical",
    "Alex Karp has said Palantir's software is used, in his own words, 'on occasion, to kill people'.",
    "Alex Karp has said Palantir's software is never used in military operations.",
    "Karp has described the software as used 'on occasion, to kill people', a statement widely quoted by critics and press.",
    ["on occasion, to kill people"])
# ---- Careers
add("glassdoor", "how-hard-is-it-to-get-a-job-at-palantir",
    "Glassdoor data rates Palantir's overall interview difficulty at roughly 3.3 out of 5.",
    "Glassdoor data rates Palantir's overall interview difficulty at roughly 1.3 out of 5.",
    "Aggregate Glassdoor data puts it at roughly 3.3 out of 5.",
    ["3.3 out of 5"])
add("hiretime", "how-hard-is-it-to-get-a-job-at-palantir",
    "Reported hiring timelines at Palantir run around 28-29 days from first contact to decision.",
    "Reported hiring timelines at Palantir run around 3 days from first contact to decision.",
    "The reported average is around 28-29 days, longer than several peers.",
    ["28-29 days"])
add("decomp", "what-are-common-palantir-interview-questions",
    "Palantir interviews often include 'decomposition' rounds testing how you break down an ambiguous problem.",
    "Palantir interviews rely mainly on memorized, textbook algorithm questions with one correct answer.",
    "A recurring format is the decomposition round, which tests comfort with ambiguity rather than one right answer.",
    ["decomposition"])
