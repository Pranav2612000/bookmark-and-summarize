import requests

licence_key = "1a680fdbb39913433f80cd0b47c8ecad"

def get_summary(article):

    # Create the request body to be sent
    request_body = {
        "key":licence_key,
        "of":"json",
        "txt":article,
        "sentences":"10"
    }
    response = requests.post("https://api.meaningcloud.com/summarization-1.0", request_body)
    summarized_resp = response.json()

    summary = summarized_resp["summary"]
    return summary

if __name__ == '__main__':
    text = '''
 Stephen Reucroft in the Elementary Particle Physics group at Northeastern University gives this introductory reply:
    "Over the past few decades, particle physicists have developed an elegant theoretical model (the Standard Model) that gives a framework for our current understanding of the fundamental particles and forces of nature. One major ingredient in this model is a hypothetical, ubiquitous quantum field that is supposed to be responsible for giving particles their masses (this field would answer the basic question of why particles have the masses they do--or indeed, why they have any mass at all). This field is called the Higgs field. As a consequence of wave-particle duality, all quantum fields have a fundamental particle associated with them. The particle associated with the Higgs field is called the Higgs boson.
    "Because the Higgs field would be responsible for mass, the very fact that the fundamental particles do have mass is regarded by many physicists as an indication of the existence of the Higgs field. We can even take all our data on particle physics data and interpret them in terms of the mass of a hypothetical Higgs boson. In other words, if we assume that the Higgs boson exists, we can infer its mass based on the effect it would have on the properties of other particles and fields. We have not yet truly proved that the Higgs boson exists, however. One of the main aims of particle physics over the next couple of decades is to prove once and for all the existence or nonexistence of the Higgs boson.""
     Another, more extensive response comes from Howard Haber and Michael Dine, both of whom are professors of physics at the Santa Cruz Institute for Particle Physics at the University of California at Santa Cruz:

    "Much of today's research in elementary particle physics focuses on the search for a particle called the Higgs boson. This particle is the one missing piece of our present understanding of the laws of nature, known as the Standard Model. This model describes three types of forces: electromagnetic interactions, which cause all phenomena associated with electric and magnetic fields and the spectrum of electromagnetic radiation; strong interactions, which bind atomic nuclei; and the weak nuclear force, which governs beta decay--a form of natural radioactivity--and hydrogen fusion, the source of the sun's energy. (The Standard Model does not describe the fourth force, gravity.)
    
    "In our daily lives, electromagnetism is the most familiar of these forces. Until relatively recently, it was the only one which we understood well. Since the 1970s, however, scientists have come to understand the strong and weak forces almost equally well. In the past few years, in high-energy experiments at CERN, the European laboratory for particle physics, near Geneva and at the Stanford Linear Accelerator Center (SLAC), physicists have made precision tests of the Standard Model. It seems to provide a complete description of the natural world down to scales on the order of one- thousandth the size of an atomic nucleus.

    "The Higgs particle is connected with the weak force. Electromagnetism describes particles interacting with photons, the basic units of the electromagnetic field. In a parallel way, the modern theory of weak interactions describes particles (the W and Z particles) interacting with electrons, neutrinos, quarks and other particles. In many respects, these particles are similar to photons. But they are also strikingly different. The photon probably has no mass at all. From experiments, we know that a photon can be no more massive than a thousand-billion-billion-billionth (10 -30) the mass of an electron, and for theoretical reasons, we believe it has exactly zero mass. The W and Z particles, however, have enormous masses: more than 80 times the mass of a proton, one of the constituents of an atomic nucleus. 
    
    "The huge masses of the W and Z particles is a puzzle. If one simply postulates that these particles interact with the known elementary particles and have a large mass, the theory is inconsistent. ( For example, the Standard Model would predict that the probability of two particles having very high energies colliding with one another would be greater than one, a physical impossibility! ) To fix this problem, there must be additional particles. The simplest models that explain the masses of the W and Z have only one such particle: the Higgs boson. There are also other proposals, many of them more exotic. For instance, there may be several Higgs bosons, entirely new types of strong interactions and a possible new fundamental physical symmetry, called supersymmetry.
    Advertisement

    "If there is a Higgs boson whose mass is less than that of the Z particle, physicists will discover it over the next two years at the large accelerator in Geneva known as LEP (the Large Electron Positron collider). LEP accelerates electrons and their antimatter twins (positrons) to very high energies, then allows them to collide. If Higgs bosons have larger masses, they might be unveiled at the Fermi National Accelerator Laboratory in Batavia, Ill., by the turn of the century. Otherwise we are very likely to find them at a new accelerator, LHC (the Large Hadron Collider), scheduled to start operation at CERN in 2005. Discovery of the Higgs boson was one of the principal tasks scheduled for the Superconducting Super Collider, which the U.S. Congress canceled in 1993.
    
    "In sum, the Higgs boson is a critical ingredient to complete our current understanding of the Standard Model, the theoretical edifice of particle physics. Different types of Higgs bosons, if they exist, may lead us into new realms of physics beyond the Standard Model."

    And Chris Quigg, a researcher in the theoretical physics department at Fermi National Accelerator Laboratory, presents a deep overview:
        newsletter promo

    Read Our Latest Issue

    "The central challenge in particle physics today is to understand what differentiates electromagnetism from the weak interactions that govern radioactivity and the energy output of the sun. The fundamental interactions between particles derive from symmetries that we have observed in nature.
    
    "One of the great recent achievements of modern physics is a quantum field theory in which weak and electromagnetic interactions are understood to arise from a common symmetry. This 'electroweak theory' has been validated in detail, especially by experiments in the LEP Collider at CERN. Although the weak and electromagnetic interactions are linked through symmetry, their manifestations in the everyday world are very different. The influence of electromagnetism extends to infinite distances, whereas the influence of the weak interaction is confined to subnuclear dimensions, less than about 10-15 centimeters. This difference is directly related to the fact that the photon, the force carrier of electromagnetism, is massless, whereas the W and Z particles, which carry the weak forces, are about 100 times the mass of the proton.
    Advertisement

    "What hides the symmetry between the weak and electromagnetic interactions? That is the question we hope to answer through experiments at the Large Hadron Collider (LHC) at CERN. When the LHC is commissioned, around the year 2005, it will enable us to study collisions among quarks at energies approaching 1 TeV, or a trillion (1012) electron volts. A thorough exploration of the 1-TeV energy scale will determine the mechanism by which the electroweak symmetry is hidden and teach us what makes the W and Z particles massive.
    
    "The simplest guess goes back to theoretical work by British physicist Peter Higgs and others in the 1960s. According to this picture, the giver of mass is a neutral particle with zero spin that we call the Higgs boson. In today's version of the electroweak theory, the W and Z particles and all the fundamental constituents--quarks and leptons--get their masses by interacting with the Higgs boson. But the Higgs boson remains hypothetical; it has not been observed. That is why particle physicists often use the search for the Higgs boson as a shorthand for the campaign to learn the agent that hides electroweak symmetry and endows other particles with mass. 

    "If the answer is the Higgs boson, we can say enough about its properties to guide the search. Unfortunately, the electroweak theory does not predict the mass of the Higgs boson, although consistency arguments require that it have a mass of less than 1 TeV. Experimental searches already carried out tell us that the Higgs must weigh more than about 60 billion electron volts (GeV), or 0.06 TeV.
    
    "If the Higgs is relatively light, it may be seen soon in electron- positron annihilations at LEP, produced in association with the Z. The Higgs boson would decay into a b quark and a b antiquark. In a few years, experiments at Fermilab's Tevatron should be able to extend the search to higher masses, looking for Higgs plus W or Higgs plus Z particles in collisions between protons and antiprotons. If the Higgs mass exceeds about 130 GeV, our best hope lies with the LHC. Higher-energy electron-positron colliders, or even muon colliders, could also play an important role.

    "Our inability to predict the mass of the Higgs boson is one of the reasons many of us believe that this picture cannot tell the whole story. We are searching for extensions to the electroweak theory that make it more coherent and more predictive. Two of these seem promising. Both of them imply that we will find a rich harvest of new particles and new phenomena at the high energies we are just beginning to explore at Fermilab and CERN. One approach is a generalization of the electroweak theory, called supersymmetry, that associates new particles with all the known quarks and leptons and force particles. Supersymmetry entails several Higgs bosons, and one of which probably lies in the energy regime that LEP is starting to survey. In the other approach, called dynamical symmetry breaking, the Higgs boson is not an elementary particle but a composite whose properties we may hope to compute once we understand its constituents and their interactions.
    Advertisement
    
    "Over the next 15 years, we should begin to find a real understanding of the origin of mass. The interest lies not just in the arcana of accelerator experiments but suffuses everything in the world around us: mass is what determines the range of forces and sets the scale of all the structures we see in nature.

    "In 1993 British Science Minister William Waldegrave challenged particle physicists to explain on a single page what the Higgs boson is and why they are so eager to find it. He awarded bottles of champagne to the authors of five winning entries at the annual meeting of the British Association for the Advancement of Science. The prizewinning papers range from serious to whimsical. They appeared in the September 1993 issue of Physics World, the monthly magazine of the British Institute of Physics, and are available online.
    
    For more on the Higgs particle, check out the Scientific American ebook, The Higgs Boson: Searching for the God Particle.
    Rights & Permissions
    Read This Next
    Sponsored
    The vast potential of atomic-scale microscopy
    '''
    summary = get_summary(text)
    print(summary)
