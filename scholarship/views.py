from django.shortcuts import render

def scholarship_list(request):
    scholarships = [
        {
            'id': 1,
            'title': 'National Merit Scholarship',
            'description': 'For high-achieving students based on academic performance.',
            'deadline': '2026-12-31',
            'amount': '$5,000',
        },
        {
            'id': 2,
            'title': 'STEM Excellence Grant',
            'description': 'For students pursuing science, technology, engineering, or mathematics.',
            'deadline': '2026-11-15',
            'amount': '$3,000',
        },
    ]

    return render(
        request,
        'accounts/scholarship_list.html',
        {'scholarships': scholarships}
    )


def scholarship_apply(request, scholarship_id):
    context = {
        'scholarship_id': scholarship_id,
        'scholarship_title': 'National Merit Scholarship',
    }

    return render(request, 'accounts/scholarship_apply.html', context)