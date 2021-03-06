"""
All static variables used in the system

Author: Himanshu Shankar (https://himanshus.com)
"""

NEW = "N"
ACCEPTED = "A"
REJECTED = "RJ"
CANCELLED = "C"
READY = "R"
PICKED_UP = "P"
OUT_FOR_DELIVERY = "O"
DELIVERED = "D"

STATUS_CHOICES = (
    (NEW, "New"),
    (ACCEPTED, "Accepted"),
    (REJECTED, "Rejected"),
    (CANCELLED, "Cancelled"),
    (READY, "Ready"),
    (PICKED_UP, "Picked Up"),
    (OUT_FOR_DELIVERY, "Out for Delivery"),
    (DELIVERED, "Delivered"),
)

DELIVERY_TYPE_CHOICES = (
    (PICKED_UP, "PICK UP"),
    (DELIVERED, "DELIVER")
)

INDIVIDUAL_PROPRIETORSHIP = "I"
PRIVATE_LIMITED = "PL"
LIMITED = "L"
LIMITED_LIABILITY_PARTNERSHIP = "LLP"
PARTNERSHIP = "P"

BUSINESS_TYPE_CHOICES = (
    (INDIVIDUAL_PROPRIETORSHIP, "Individual/Proprietorship"),
    (PRIVATE_LIMITED, "Private Limited"),
    (LIMITED, "Limited (Public Company)"),
    (LIMITED_LIABILITY_PARTNERSHIP, "Limited Liability Partnership (LLP)"),
    (PARTNERSHIP, "Partnership"),
)

FSSAI = "F"
PAN = "P"
AADHAR = "A"
DRIVING_LICENSE = "D"
VOTER_ID = "V"
CERTIFICATE_OF_INCORPORATION = "COI"
TAN = "T"
GST = "G"
MEMORANDUM_OF_ASSOCIATION = "MOA"
AGREEMENT_OF_ASSOCIATION = "AOA"
RENTAL_AGREEMENT = "RA"
PREVIOUS_EMPLOYER_CERTIFICATE = "PEC"
EDUCATION_CERTIFICATE = "EDU"
OFFER_LETTER = "OFR"
NON_DISCLOSURE_AGREEMENT = "NDA"
PICTURE = "PIC"

BUSINESS_DOCUMENT_CHOICES = (
    (FSSAI, "FSSAI License"),
    (PAN, "Pan Card"),
    (AADHAR, "AADHAR Card"),
    (CERTIFICATE_OF_INCORPORATION, "Certificate of Incorporation"),
    (TAN, "TAN Card"),
    (GST, "GST Registration"),
    (MEMORANDUM_OF_ASSOCIATION, "Memorandum of Association"),
    (AGREEMENT_OF_ASSOCIATION, "Agreement of Association"),
    (RENTAL_AGREEMENT, "Rental Agreement"),
)

EMPLOYEE_DOCUMENT_CHOICES = (
    (PAN, "Pan Card"),
    (AADHAR, "AADHAR Card"),
    (DRIVING_LICENSE, "Driving License"),
    (VOTER_ID, "Voter ID"),
    (PREVIOUS_EMPLOYER_CERTIFICATE, "Previous Employer Certificate"),
    (EDUCATION_CERTIFICATE, "Education Certificate"),
    (OFFER_LETTER, "Offer Letter"),
    (NON_DISCLOSURE_AGREEMENT, "Non Disclosure Agreement"),
    (PICTURE, "Picture")
)

VERIFIED = "V"
PENDING = "P"
VERIFICATION_FAILED = "F"

DOCUMENT_STATUS_CHOICES = (
    (VERIFICATION_FAILED, "Verification Failed"),
    (PENDING, "Pending Verification"),
    (VERIFIED, "Verified"),
)

PAID = "P"
UNPAID = "U"

BILL_STATUS_CHOICES = (
    (PAID, "Paid"),
    (UNPAID, "UnPaid"),
)

ON_COUNTER = "C"
ONLINE = "O"

PAYMENT_TYPE_CHOICES = (
    (ON_COUNTER, "On Counter"),
    (ONLINE, "Online"),
)

CREDIT_CARD = "CC"
DEBIT_CARD = "DC"
PAYTM = "PTM"
CASH = "C"
INSTAMOJO = "IMJ"
PAYTM_GATEWAY = "PTMG"

PAYMENT_MODE_CHOICES = (
    (CREDIT_CARD, "Credit Card"),
    (DEBIT_CARD, "Debit Card"),
    (PAYTM, "PayTM"),
    (CASH, "Cash"),
    (INSTAMOJO, "Instamojo"),
    (PAYTM_GATEWAY, "PayTM Payment Gateway"),
)
