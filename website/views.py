from django.shortcuts import render

from website.models import Gallery, News, Package, Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    packages = Package.objects.all()
    news = News.objects.all()

    cards = [
        {
            'title': 'About us',
            # 'description': 'Welcome to KidzRunz!',
            'image': '',
            'link': '/about'
        },
        {
            'title': 'Our services',
            # 'description': 'Included but not limited to',
            'image': '',
            'link': '/services'
        },
        {
            'title': 'Gallery',
            # 'description': None,
            'image': '',
            'link': '/gallery'
        },
        {
            'title': 'Mentoring Activate Packages',
            # 'description': 'Packages aimed at youths',
            'image': '',
            'link': '/activities'
        }
        # {
        #     'title': 'Director\'s Story',
        #     # 'description': 'Meet Kenneth Holder',
        #     'image': '',
        #     'link': '/leadership'
        # },
        # {
        #     'title': 'Mission and Ethos',
        #     # 'description': 'To give back to the community',
        #     'image': '',
        #     'link': '/mission'
        # },
        # {
        #     'title': 'Terms and Conditions',
        #     # 'description': None,
        #     'image': '',
        #     'link': '/terms-and-conditions'
        # },
        # {
        #     'title': 'Safeguarding and Enhanced DBS',
        #     # 'description': None,
        #     'image': '',
        #     'link': '/safeguarding-and-enhanced-dbs'
        # },
        # {
        #     'title': 'Sponsors and donate',
        #     # 'description': None,
        #     'image': '',
        #     'link': ''
        # },
        # {
        #     'title': 'Who CAMS are',
        #     # 'description': 'Child Activity Mentor Support (CAMS)',
        #     'image': '',
        #     'link': '/who-cams-are'
        # },
        # {
            # 'title': 'Mindfulness approach',
            # # 'description': 'We take a mindfulness approach',
            # 'image': '',
            # 'link': '/mindfulness-approach'
        # },
        # {
        #     'title': 'CAMS PACE APPROACH',
        #     # 'description': 'Creating a safe and nurturing environment',
        #     'image': '',
        #     'link': '/cams-pace-approach'
        # },
    ]

    context = {
        'services': services,
        'packages': packages,
        'link_cards': cards,
        'news': news,
    }
    return render(request, "website/index.html", context=context)


def aboutus(request, slug):
    context = {}
    if (slug == 'welcome-to-kidzrunz'):
        context = {
            'title': 'Welcome to Kidz Runz!',
            'content': '''
        Welcome to Kidz Runz, where adventure and convenience collide!
        At Kidz Runz, we're fueled by a passion for making kids' dreams come true. We know that families and caregivers have superpowers, but even superheroes need a helping hand sometimes. That's where we come in!

        We're here to save the day by allowing your child to participate in exciting local sporting activities. We understand the chaos of busy schedules, and we've got your back. We're trying to make your life easier, so you can focus on enjoying those precious family moments.

        With Kidz Runz by your side, you'll wave goodbye to the stress of logistics and wave hello to more quality time with your little champions. Together, we'll turn ordinary days into extraordinary adventures!

        Join us at Kidz Runz and let the fun begin! It's time to unlock the full potential of your child's sporting dreams. Buckle up because we're here to make magic happen!
        '''
        }
    elif (slug == 'our-mission-statements'):
        context = {
            'title': 'Our Mission Statements',
            'content': '''
At Kidz Runz, our mission is to be the ultimate sidekick for parents and caregivers, ensuring their children always have a thrilling and active experience, even when they can't be there in person. We're here to support you every step of the way, offering comprehensive packages that cater to your child's every need. From handling transportation logistics to providing our incredible team of Child Activity Mentors, we've got you covered!

We're driven by our mission to keep your children active, engaged, and supercharged with joy. We believe in providing a reliable and safe service that ensures your child thrives in a nurturing and exhilarating environment. Together, let's embark on an incredible journey of growth, well-being, and unforgettable experiences for your child!

So, join our league of extraordinary adventurers and let Kidz Runz be your trusted sidekick. Together, we'll create magical memories and empower your child to reach new heights of excitement and discovery. Get ready for an adventure-filled ride that will leave your child beaming with happiness!
'''
            }
    elif (slug == 'once-upon-a-time-story'):
        context = {
            'title': 'Once Upon A Time Story',
            'content': '''
Once upon a time, in the cosmic town of Willowville, the Dylema family had a celestial dilemma. Mr. and Mrs. Dylema, with their three energetic kids, Jake, Lily, and Ethan, found themselves caught in a cosmic whirlwind of work, chores, and never-ending family obligations. They yearned to send their little ones on daring sporting adventures and thrilling outings. Still, the universe seemed to conspire against them, making it nearly impossible to be in multiple places simultaneously.

But fear not, for Kidz Runz emerged like a shooting star to save the day! With their intergalactic Child Activity Mentor Support (CAMS) service, they offered a celestial solution to the Dylema family's predicament.

Kidz Runz understood the importance of cosmic safety and had their CAMS mentors undergo thorough background checks, ensuring they were as reliable as a supernova. These mentors were more than just chauffeurs; they were friendly cosmic guides, creating a universe of fun and security for the children they accompanied.

Whether it was Jake's interplanetary football practices, Lily's out-of-this-world art classes, or Ethan's gravity-defying swimming lessons, Kidz Runz arranged transportation like cosmic taxis, whisking the kids away to their stellar destinations. But hold on tight! Kidz Runz didn't stop there. They orchestrated mind-boggling outings to theme parks on distant moons. They even organized one-on-one escapades to hairstyle appointments, cinemas, bowling, city break sightseeing, and theaters in far-off galaxies.

When the CAMS mentors arrived at the Dylema household, their starship-like vehicles were equipped with spacious cabins, ensuring a comfy and giggly journey through the cosmos. With games, stories, and laughter, these cosmic companions transformed each trip into a joyous adventure beyond imagination.

The Dylema parents finally breathed a sigh of relief. They no longer had to warp through space and time, trying to fit everything into their packed schedules. With Kidz Runz's cosmic support, their children could pursue their passions, make new cosmic friends, and create astronomical memories. Meanwhile, the Dylema parents could focus on their work and earthly responsibilities, knowing their little astronauts were safe.

Kidz Runz became the constellations of trust, reliability, and dedication in the Dylema family's universe. They helped create a generation of confident and healthy cosmic kids who embraced an active lifestyle and shone brighter than any star in the galaxy.

And so, in the vast expanse of their adventures, the Dylema family found solace in Kidz Runz's cosmic commitment to their children's well-being, their warp-speed transport arrangements, and their mission to make the universe a playground of discovery and joy for all young explorers.

Join us at Kidz Runz, where the cosmos becomes your playground, and your child's dreams reach for the stars! Let the cosmic adventures begin!
'''
            }
    elif (slug == 'when-you-choose-kidz-runz'):
        context = {
            'title': 'When you choose Kidz Runz',
            'content': '''
Prepare for an astronomical Kidz Runz mission to launch you into a galaxy of laughter and zero-gravity fun! Strap tight and prepare for an adventure like no other. Our extraordinary team of Child Activity Mentors is here to accompany you on a cosmic journey tailored to your unique interests.

These mentors aren't your everyday guides – they're like magical space buddies who will transform each moment into an interstellar quest filled with laughter, discovery, and cosmic joy! With their unwavering commitment to safety and their superpowers of creating unforgettable memories, they guarantee a secure and mind-blowing experience for every young adventurer they accompany.

But hold on tight, my fellow space explorers! We know that traversing the vast universe can work up an appetite. Fear not; our starships are stocked with an incredible selection of nutritious snacks and cosmic beverages that will keep your energy levels soaring as you conquer new challenges and forge intergalactic memories that are truly out of this world!

So gear up, suit up, and prepare for the most heart-pounding adventure of your cosmic lives! When you choose Kidz Runz, prepare for excitement, laughter, and memories that will make your friends on Mars turn green with envy. Your happiness and well-being are our highest priorities, and our phenomenal team of Child Activity Mentors is dedicated to ensuring that every moment is extraordinary, every outing is an absolute blast, and every memory sparkles like a shooting star. Fellow space explorers, it's time to ignite your thrusters and launch into the thrilling universe of Kidz Runz! 3... 2... 1... Ignition! Let the cosmic adventure begin!
'''
            }
    elif (slug == 'communication-and-feedback'):
        context = {
            'title': 'Communication and feedback',
            'content': '''
Attention, cosmic adventurers and Earthly parents! Get ready for a communication and feedback system that's out of this world at Kidz Runz! We're not just about shuttling kids from point A to point B. Oh no, we're your trusty intergalactic partners on the wildest adventure of a lifetime!

Picture this: we've formed an elite alliance with coaches and teachers, gathering all the insider information on your child's cosmic sessions. We've got the inside scoop on every jump, every swim, and every goal. Why? So we can give you, the cosmic parents, the lowdown on all the mind-blowing progress and jaw-dropping accomplishments your little superheroes achieve!

Transparency and open communication are our secret weapons in this cosmic journey. We believe in keeping you, the superhero parents, in the loop so you can enjoy all the cosmic fun. Trust is built on knowing what's happening, and we're here to make sure you're well-informed about every warp-speed twist and gravity-defying turn in your child's adventure.

At Kidz Runz, we're more than just a ride – we're your reliable sidekicks, your cosmic confidants. We're all about supporting families and helping your incredible kids unleash their hidden superpowers. Our pride and joy come from our commitment to professionalism, reliability, and your child's well-being.

So buckle up, fellow space explorers, and let's embark on this cosmic adventure together! With Kidz Runz by your side, get ready to witness your child's star power shine brighter than the brightest supernova. Let's ignite the engines of communication, zoom through the galaxy of progress updates, and watch your little heroes conquer the universe!
'''
            }
    elif (slug == 'parent-tips-and-support'):
        context = {
            'title': 'Parent Tips and Support',
            'content': '''
Therapy information will assist you in nurturing your child's well-being and creating a positive family experience. If you have any questions or need more help, please don't hesitate to contact our team. We are here to support you every step of the way!

Parent Tips:

1. Establishing a Routine: We understand the importance of creating a structured routine for your child. Setting consistent bedtimes, meal times, and designated study or play times provides a predictable and balanced daily routine that helps your child feel secure and stable.

2. Effective Communication is key to fostering a strong parent-child bond. We encourage open and honest communication with your child, creating a safe space where they feel comfortable expressing their thoughts, feelings, and concerns. Active listening and validating their emotions are crucial elements of effective communication.

3. Encouraging Physical Activity: We believe in the power of regular physical activity for your child's overall well-being. Not only does it benefit their physical health, but it also promotes mental wellness. Encourage outdoor play, sports, or family walks to instill an active lifestyle and make physical activity enjoyable for your child.

4. Promoting Healthy Habits: Teaching your child healthy habits is a valuable life lesson. From proper nutrition to regular sleep patterns and personal hygiene, these habits contribute to their overall well-being and can help prevent illnesses. Instilling healthy habits early on sets the foundation for a healthier future.

5. Nurturing Emotional Intelligence: Emotional intelligence is vital for your child's development. Helping them identify and manage their emotions is essential. Encourage empathy, self-reflection, and problem-solving skills to enhance their emotional well-being and improve their social interactions.

Support Services for Children and Families:

1. Counseling Services: We understand that sometimes children and families face emotional, behavioral, or relationship challenges. Our professional counseling services provide a safe and supportive environment where trained therapists offer guidance and techniques to navigate difficult situations and promote positive mental health.

2. Parenting Workshops and Support Groups: Parenting is a rewarding journey but can be challenging. That's why we offer parenting workshops and support groups. These resources provide valuable insights, guidance, and a network of like-minded individuals who share their experiences and knowledge. It's an opportunity to build supportive relationships and gain valuable parenting skills.

3. Educational Support: If your child requires additional academic support, we recommend seeking educational services such as tutoring or specialized programs tailored to their needs. These services can enhance learning, boost confidence, and address specific learning challenges, ensuring your child reaches their full potential.

4. Community Resources: We encourage you to explore local community resources that offer activities and support services for children and families. Recreational programs, libraries, and community centers often provide opportunities for socialization, skill development, and access to information and assistance. These resources can be invaluable in enriching your child's life and supporting your family.

Information on Therapy:

Therapy can be a valuable resource for children and families facing various challenges. Here are some types of therapy that may be beneficial:

1. Play Therapy: Play therapy utilizes play and creative activities to help children express their emotions, improve communication, and develop problem-solving skills in a supportive therapeutic setting. It's a fun and effective way for children to work through challenges and develop coping mechanisms.

2. Cognitive-Behavioral Therapy (CBT) focuses on identifying and modifying negative thoughts and behaviors to promote positive changes in emotional well-being and behavior patterns. It equips children with valuable skills to manage their emotions and overcome obstacles.

3. Family Therapy involves working with the entire family unit to address relationship dynamics, improve communication, and resolve conflicts. It can strengthen family bonds and create a supportive environment for everyone involved.

4. Art Therapy: Art therapy harnesses the power of creativity to help children communicate their emotions, reduce stress, and promote self-discovery and personal growth. Through artistic expression, children can explore their feelings and find new ways to express themselves.

Every child and family is unique, and individual circumstances may require personalized approaches and interventions. Seeking professional advice and support when needed is essential, and we are here to provide transportation services and support to empower families.

At Kidz Runz, we are committed to your child's well-being and strive to be a reliable source of information and resources for parents. We hope these parent tips, support services, and therapy information will assist you in nurturing your child's development and creating a positive family experience. If you have any questions or need any more help, please don't hesitate to contact our dedicated team. We're here to support you every step of the way!
'''
            }
    elif (slug == 'our-commitment-to-safeguarding'):
        context = {
            'title': 'Our Commitment to Safeguarding',
            'content': '''
At Kidz Runz, we want to assure parents that their children's safety and well-being are our utmost priorities. We take safeguarding seriously and have implemented rigorous measures to create a secure environment. Here's how we demonstrate our commitment to safeguarding:

1. Thorough Background Checks: All staff members, including Child Activity Mentors Support (CAMS) and support workers, undergo comprehensive Enhanced Disclosure and Barring Service (DBS) checks. These checks ensure we only have trustworthy individuals suitable to work with children. Please don't worry- we carefully screen our team to ensure the safety of your children.

2. Proactive Vigilance and Reporting: We maintain a vigilant approach to safeguarding. Our staff members are trained to promptly identify and report any concerns or signs of harm. By being proactive, we can address potential risks or issues that may impact the well-being of children or their families. If any concerns arise, we have robust reporting procedures to take immediate action and protect those involved.

3. Confidentiality and Privacy: We understand the importance of confidentiality and privacy when safeguarding matters. Any information shared with us will be handled carefully, adhering to legal requirements and data protection guidelines. Your trust is essential, and we prioritize maintaining a secure environment where children and families feel comfortable sharing their concerns.

4. Collaboration and Support: Kidz Runz believes in collaboration and strong partnerships. We work closely with relevant authorities such as social services, schools, and other child protection agencies. By working together, we ensure a coordinated and effective approach to safeguarding. We value the input of families and caregivers and actively involve them in the safeguarding process, creating a supportive network to address concerns and provide assistance when needed.

5. Ongoing Training and Development: Our staff members receive regular training and development sessions to enhance their knowledge of safeguarding practices. This includes staying up-to-date on current legislation, recognizing signs of abuse or neglect, and implementing appropriate preventive measures. By investing in continuous training, we ensure that our team remains well-equipped to protect the welfare of children and families.

6. Open Communication: We encourage open and transparent communication with children, families, and caregivers. We believe in maintaining a trusting relationship where concerns can be expressed and promptly handled. By fostering open communication, we create a safe and inclusive environment where everyone feels heard and supported.

At Kidz Runz, safeguarding is not just a legal obligation but the foundation of our service. We are dedicated to providing a safe, nurturing, and enriching experience for every child in our care. With our high safeguarding standards, we aim to create an environment where children and families can thrive with confidence and peace of mind.

If you have any concerns or become aware of any issues related to the welfare of children and families in our care, please don't hesitate to contact us. Together, we can ensure the well-being and protection of every child we serve.
'''
            }
    return render(request, "website/about-us.html", context=context)


def contactus(request):
    return render(request, "website/contact-us.html")


def faqs(request):
    return render(request, "website/faqs.html")


def consultation(request):
    return render(request, "website/consultation.html")


def leadership(request):
    return render(request, "website/leadership.html")


def mission(request):
    return render(request, "website/mission.html")


def services(request):
    return render(request, "website/services.html")


def termsandconditions(request):
    return render(request, "website/terms-and-conditions.html")


def privacy_policy(request):
    return render(request, "website/privacy-policy.html")


def safeguardingandenhanceddbs(request):
    return render(request, "website/safeguarding-and-enhanced-dbs.html")


def gallery(request):
    context = {
        'gallery': Gallery.objects.all(),
    }
    return render(request, "website/gallery.html", context=context)


def activities(request):
    packages = Package.objects.all()

    context = {
        'packages': [{
            'name': package.name,
            'image': package.image,
            'price': package.price,
            'duration': package.duration,
            'description': package.description.splitlines(),
        } for package in packages]
    }
    return render(request, "website/activities.html", context)


def who_cams_are(request):
    return render(request, "website/who-cams-are.html")


def mindfuless_approach(request):
    return render(request, "website/mindfulness-approach.html")


def cams_pace_approach(request):
    return render(request, "website/cams-pace-approach.html")


def blog(request):
    context = {
        'posts': News.objects.all()
    }
    return render(request, "website/blog.html", context=context)


def blog_details(request, slug):
    context = {
        'posts': News.objects.exclude(slug=slug).all(),
        'post': News.objects.get(slug=slug)
    }
    return render(request, "website/blog-details.html", context=context)
