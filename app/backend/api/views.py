from django.http import JsonResponse


def hello(request):

    livres = [
        {
            "titre": "Clean Code",
            "auteur": "Robert C. Martin"
        },
        {
            "titre": "Design Patterns: Elements of Reusable Object-Oriented Software",
            "auteur": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides"
        },
        {
            "titre": "The Pragmatic Programmer",
            "auteur": "Andrew Hunt et David Thomas"
        },
        {
            "titre": "Computer Networking: A Top-Down Approach",
            "auteur": "James F. Kurose et Keith W. Ross"
        },
        {
            "titre": "TCP/IP Illustrated, Volume 1",
            "auteur": "W. Richard Stevens"
        },
        {
            "titre": "Hacking: The Art of Exploitation",
            "auteur": "Jon Erickson"
        },
        {
            "titre": "The Web Application Hacker's Handbook",
            "auteur": "Dafydd Stuttard et Marcus Pinto"
        },
        {
            "titre": "Practical Malware Analysis",
            "auteur": "Michael Sikorski et Andrew Honig"
        },
        {
            "titre": "The Art of Electronics",
            "auteur": "Paul Horowitz et Winfield Hill"
        },
        {
            "titre": "Introduction to Algorithms",
            "auteur": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest et Clifford Stein"
        }
    ]

    return JsonResponse({
        "bibliotheque": "Bibliothèque Informatique",
        "nombre_livres": len(livres),
        "livres": livres
    })
def health(request):
    return JsonResponse({
        "status": "UP"
    })


# Create your views here.
