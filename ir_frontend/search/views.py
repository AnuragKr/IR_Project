from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from search import settings
from .service import RetriveResults


# Create your views here.

def search(request):
    return render(request, 'search2.html')

def search_by_fiels(request):
    return render(request, 'search.html')

def results(request):
    if request.method == 'POST':
        query = request.POST['query']
        scoring_model= request.POST['scoring_model']
        search_field = request.POST['field']
        
        # print(query, scoring_model, search_field)

        request.session['query'] = query
        request.session['scoring_model'] = scoring_model
        request.session['search_field'] = search_field
        
        if search_field == '':
            search_request = {
                "model":scoring_model,
                "is_field_query":0,
                "query":query}
            #print(request)
        
        else:
            search_request = {
                    "model":scoring_model,
                    "is_field_query":1,
                    "query":{search_field:query}
                    }
        print(search_request)


        get_results = RetriveResults()
        results = get_results.get_results_by_field_query(search_request)
        print(results)
        # results = {
        #      'search_result':[ 
        #              {
        #                 "movie_name": "Black Panther: Wakanda Forever",
        #                 "year": 2022,
        #                 "rating": "PG-13",
        #                 "genre": "Action, Adventure, Drama",
        #                 "runtime_min": 161,
        #                 "imdb": 7.3,
        #                 "metascore": 67,
        #                 "votes": 105152,
        #                 "image_link": "https://m.media-amazon.com/images/M/MV5BNTM4NjIxNmEtYWE5NS00NDczLTkyNWQtYThhNmQyZGQzMjM0XkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_UX67_CR0,0,67,98_AL_.jpg",
        #                 "movie_link": "https://en.wikipedia.org/wiki/Black Panther: Wakanda Forever",
        #                 "plot": "T'Challa, king of Wakanda, is dying from an illness which his sister, Shuri, believes can be cured by the \"heart-shaped herb\". Shuri attempts to synthetically recreate the herb after it was destroyed by Erik Killmonger,[N 1] but fails to do so before T'Challa succumbs.\nOne year later, Wakanda is under pressure from other nations to share their vibranium, with some parties attempting to steal it by force. Queen Ramonda implores Shuri to continue her research on the heart-shaped herb, hoping to create a new Black Panther that will defend Wakanda, but she refuses due to her belief that the Black Panther is a figure of the past. In the Atlantic Ocean, the CIA and U.S. Navy SEALs utilize a vibranium-detecting machine to locate a potential vibranium deposit underwater. The expedition is attacked and killed by a group of blue-skinned, water-breathing superhumans led by Namor, with the CIA believing Wakanda to be responsible. Namor confronts Ramonda and Shuri, easily bypassing Wakanda's advanced security. Blaming Wakanda for the vibranium race, he gives them an ultimatum: deliver him the scientist responsible for the vibranium-detecting machine, or he will attack Wakanda.\nShuri and Okoye learn from CIA agent Everett K. Ross that the scientist in question is MIT student Riri Williams and arrive at the university to confront her. The group is pursued by the FBI and then by Namor's warriors, who defeat Okoye before taking Shuri and Williams underwater to meet Namor. Angered by Okoye's failure to protect Shuri, Ramonda strips her of her title as general of the Dora Milaje and seeks out Nakia, who has been living in Haiti since Thanos's attack on Wakanda.[N 2] Namor shows Shuri his vibranium-rich underwater kingdom of Talokan, which he has protected for centuries from discovery by the world. Bitter at the surface world for enslaving the Maya, Namor proposes an alliance with Wakanda against the rest of the world but threatens to destroy Wakanda if they refuse. Nakia helps Shuri and Williams escape, and Namor retaliates with an attack against Wakanda, during which Ramonda drowns saving Williams. Namor vows to return with his full army, and the citizens of Wakanda relocate to the Jabari mountains for their safety. Meanwhile, Ross is arrested by his ex-wife, CIA director Valentina Allegra de Fontaine, for secretly exchanging classified intelligence with the Wakandans.\nAfter Ramonda's funeral, Shuri uses a remnant of the herb that gave Namor's people their superhuman abilities to reconstruct the heart-shaped herb. She ingests it, gaining superhuman abilities and meeting Killmonger in the Ancestral Plane, who urges her to seek revenge. Shuri dons a new Black Panther suit and is accepted by the other Wakandan tribes as the Black Panther. Despite M'Baku's urges for peace, Shuri is determined to exact vengeance on Namor for Ramonda's death and orders an immediate counterattack on Talokan. Preparing for battle, with Ayo assuming the position of general of the Dora Milaje, Shuri bestows the Midnight Angel armor upon Okoye, who in turn recruits Dora Milaje member Aneka to join her. Williams creates an Iron Man-esque powered exoskeleton to aid the Wakandans.\nUsing a seafaring vessel, the Wakandans lure Namor and his warriors to the surface as a battle ensues. Shuri traps Namor in a fighter aircraft, intending to dry him out and weaken him. The pair crashes on a desert beach and fight. Shuri gains the upper hand, but realizes the similarities between their paths and implores Namor to yield, offering him a peaceful alliance. Namor accepts, and the battle ends. Namor's cousin, Namora, is upset at Namor's surrender, but he assures her that the new alliance will allow them to conquer the surface world one day. Williams returns to MIT, leaving her suit behind, while Okoye rescues Ross from captivity. Shuri plants more heart-shaped herbs to ensure the future of the Black Panther mantle. In Shuri's absence, M'Baku steps forward to challenge for the throne. Shuri visits Nakia in Haiti where she burns her funeral ceremonial robe in accordance with Ramonda's wishes, allowing herself to finally grieve T'Challa.\nIn a mid-credits scene, Shuri learns that Nakia and T'Challa had a son named Toussaint, who Nakia has been raising in secret. Toussaint reveals his Wakandan name is T'Challa.\n",
        #                 "abstract": "Black Panther: Wakanda Forever is a 2022 American superhero film based on the Marvel Comics character Black Panther. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures, it is the sequel to Black Panther (2018) and the 30th film in the Marvel Cinematic Universe (MCU). Directed by Ryan Coogler, who co-wrote the screenplay with Joe Robert Cole, the film stars Letitia Wright as Shuri / Black Panther, alongside Lupita Nyong'o, Danai Gurira, Winston Duke, Florence Kasumba, Dominique Thorne, Michaela Coel, Tenoch Huerta Mej\u00eda, Martin Freeman, Julia Louis-Dreyfus, and Angela Bassett. In the film, the leaders of Wakanda fight to protect their nation in the wake of King T'Challa's death.\nIdeas for a sequel began after the release of Black Panther in February 2018. Coogler negotiated to return as director in the following months, and Marvel Studios officially confirmed the sequel's development in mid-2019. Plans for the film changed in August 2020 when Black Panther star Chadwick Boseman died from colon cancer, with Marvel choosing not to recast his role of T'Challa. Other main cast members from the first film were confirmed to return by that November, and the title was announced in May 2021. Production initially took place from late June to early November 2021, in Atlanta and Brunswick, Georgia, as well as around Massachusetts, before a hiatus to allow Wright to recover from an injury sustained during filming. Production resumed by mid-January 2022 and wrapped in late March in Puerto Rico.\nBlack Panther: Wakanda Forever premiered at the El Capitan Theatre and the Dolby Theatre in Hollywood on October 26, 2022, and was released in the United States on November 11, 2022, as the final film in Phase Four of the MCU. The film received positive reviews from critics, with praise towards Coogler's direction, the action sequences, production and costume design, the cast's performances (particularly those of Wright, Gurira, Huerta, and Bassett), emotional weight, musical score, and its tributes to Boseman, although the runtime received some criticism. The film has grossed over $684 million worldwide, becoming the seventh-highest-grossing film of 2022.\n"
        #             }
        #     ]
        # }
        data = results['search_result']
        tot_retrieved = results['retrieved_doc_no']
        return render(request, 'results.html', {'query':query, 'data':data, 'tot_retrieved':tot_retrieved})

    if request.method == 'GET':
        query = request.session['query']
        scoring_model = request.session['scoring_model'] 
        search_field = request.session['search_field'] 
        
        if search_field == '':
            search_request = {
                "model":scoring_model,
                "is_field_query":0,
                "query":query}
            
        
        else:
            search_request = {
                    "model":scoring_model,
                    "is_field_query":1,
                    "query":{search_field:query}
                    }
        print(search_request)


        get_results = RetriveResults()
        results = get_results.get_results_by_field_query(search_request)
        print(results)
        data = results['search_result']
        tot_retrieved = results['retrieved_doc_no']
        return render(request, 'results.html', {'query':query, 'data':data, 'tot_retrieved':tot_retrieved})

# /search/?query=

def get_suggesions(request):

    query = request.GET.get('query')
    payloads = [query]
    get_results = RetriveResults()
    results = get_results.get_auto_suggetions({'query':query})
    #print(results)
    data = results['search_result']
    for d in data:
        payloads.append(d['movie_name'])
    
    print(payloads)
    #payloads.extend(['most popular movies', 'black panther movie', 'most popular actor'])
    
    return JsonResponse({'status':200, 'data':payloads})

def show_results(request):
    query = request.GET.get('query')
    print(query)
    get_results = RetriveResults()
    results = get_results.get_results_by_BM25({'query':query})
    print(results)
    data = results['search_result']
    tot_retrieved = results['retrieved_doc_no']
    return render(request, 'results.html', {'query':query, 'data':data, 'tot_retrieved':tot_retrieved})



