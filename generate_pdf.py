import os
from fpdf import FPDF

class PitchDeckPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="landscape", unit="mm", format="A4")
        self.set_margins(15, 15, 15)
        self.set_auto_page_break(False)
        
    def header(self):
        if self.page_no() > 1:
            # Header bar
            self.set_fill_color(17, 24, 39) # Dark Slate Gray
            self.rect(0, 0, 297, 12, "F")
            
            # Brand Header text
            self.set_text_color(243, 244, 246) # Off-white
            self.set_font("Helvetica", "B", 8)
            self.text(15, 8, "DC SEWING MACHINES  |  JOINT VENTURE PARTNERSHIP PITCH")
            
            # Thin divider
            self.set_draw_color(245, 158, 11) # Gold Accent
            self.set_line_width(0.5)
            self.line(0, 12, 297, 12)

    def footer(self):
        if self.page_no() > 1:
            # Thin top border for footer
            self.set_draw_color(229, 231, 235) # Light gray
            self.set_line_width(0.3)
            self.line(15, 195, 282, 195)
            
            # Page Number
            self.set_text_color(156, 163, 175) # Muted Gray
            self.set_font("Helvetica", "", 8)
            self.text(275, 201, f"Page {self.page_no()}")
            self.text(15, 201, "Confidential  |  Prepared for the Business Owner")

    def draw_slide_layout(self, title, bullets, visual_title, visual_lines, quote):
        # 1. Slide Title
        self.set_y(22)
        self.set_x(15)
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(17, 24, 39) # Dark text
        self.cell(0, 10, title, ln=True)
        
        # Gold accent line below title
        self.set_draw_color(245, 158, 11) # Gold
        self.set_line_width(1.5)
        self.line(15, 33, 120, 33)
        
        # 2. Bullets Column (Left)
        self.set_y(42)
        self.set_font("Helvetica", "", 12)
        self.set_text_color(55, 65, 81) # Charcoal
        
        col_width = 160
        bullet_spacing = 8
        
        for bullet in bullets:
            self.set_x(15)
            # Draw a nice custom bullet marker (square or dash)
            self.set_fill_color(20, 184, 166) # Teal
            self.rect(15, self.get_y() + 1.5, 2, 2, "F")
            
            # Bullet Text
            self.set_x(20)
            self.multi_cell(col_width - 5, 6, bullet, border=0, align="L")
            self.set_y(self.get_y() + bullet_spacing)
            
        # 3. Visual Callout Box (Right)
        # Background box
        self.set_fill_color(249, 250, 251) # Very light gray
        self.set_draw_color(229, 231, 235) # Light gray border
        self.set_line_width(0.5)
        self.rect(185, 42, 97, 100, "DF")
        
        # Visual Header
        self.set_y(47)
        self.set_x(190)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(17, 24, 39)
        self.cell(87, 8, visual_title, ln=True, align="C")
        
        # Visual divider line
        self.set_draw_color(20, 184, 166) # Teal Accent
        self.set_line_width(1)
        self.line(195, 55, 272, 55)
        
        # Visual Content Lines
        self.set_y(60)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(75, 85, 99)
        for line in visual_lines:
            self.set_x(190)
            # Check if it is a subheader inside the visual
            if line.startswith("**") and line.endswith("**"):
                self.set_font("Helvetica", "B", 10)
                self.set_text_color(17, 24, 39)
                clean_line = line.replace("**", "")
                self.cell(87, 6, clean_line, ln=True, align="L")
                self.set_font("Helvetica", "", 10)
                self.set_text_color(75, 85, 99)
            elif line.strip() == "---":
                y_pos = self.get_y() + 3
                self.set_draw_color(229, 231, 235)
                self.line(195, y_pos, 272, y_pos)
                self.set_y(y_pos + 3)
            else:
                self.multi_cell(87, 5, line, border=0, align="L")
                self.set_y(self.get_y() + 2)

        # 4. Quote Callout Box (Bottom)
        self.set_fill_color(245, 158, 11) # Gold background for quote card
        # Or a soft cream background with gold border
        self.set_fill_color(255, 251, 235) # Soft amber cream
        self.set_draw_color(251, 191, 36) # Amber border
        self.set_line_width(0.5)
        self.rect(15, 155, 267, 22, "DF")
        
        # Quote Text
        self.set_y(159)
        self.set_x(20)
        self.set_font("Helvetica", "BI", 11)
        self.set_text_color(146, 64, 14) # Rich amber text
        self.cell(257, 6, f'"{quote}"', align="C")

def create_pitch_deck():
    pdf = PitchDeckPDF()
    
    # ---------------------------------------------------------
    # PAGE 1: TITLE COVER SLIDE
    # ---------------------------------------------------------
    pdf.add_page()
    
    # Background decorations (Geometric panels matching web app design)
    pdf.set_fill_color(10, 12, 16) # Rich dark background
    pdf.rect(0, 0, 297, 210, "F")
    
    # Gold accent line on cover left
    pdf.set_fill_color(245, 158, 11)
    pdf.rect(0, 0, 8, 210, "F")
    
    # Cover Content
    pdf.set_y(60)
    pdf.set_x(25)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(20, 184, 166) # Teal
    pdf.cell(0, 8, "STRATEGIC DIGITAL TRANSFORMATION PROPOSAL", ln=True)
    
    pdf.set_y(70)
    pdf.set_x(25)
    pdf.set_font("Helvetica", "B", 32)
    pdf.set_text_color(255, 255, 255) # White
    pdf.multi_cell(240, 14, "Unlocking the Next Chapter\nfor DC Sewing Machines", border=0, align="L")
    
    # Underline decoration
    pdf.set_fill_color(245, 158, 11) # Gold
    pdf.rect(25, 105, 80, 2, "F")
    
    pdf.set_y(120)
    pdf.set_x(25)
    pdf.set_font("Helvetica", "", 16)
    pdf.set_text_color(209, 213, 219) # Light gray
    pdf.cell(0, 8, "A Digital Revenue-Share Joint Venture Partnership", ln=True)
    
    pdf.set_y(160)
    pdf.set_x(25)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(156, 163, 175) # Muted gray
    pdf.cell(0, 5, "PREPARED BY: Remote Digital Expert", ln=True)
    pdf.set_x(25)
    pdf.cell(0, 5, "PREPARED FOR: The Business Owner of DC Sewing Machines", ln=True)
    pdf.set_x(25)
    pdf.cell(0, 5, "LOCATION: 1774 Pershore Rd, Birmingham, B30 3BG  |  DATE: July 2026", ln=True)

    # ---------------------------------------------------------
    # PAGE 2: DECOUPLING ASSETS
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.draw_slide_layout(
        title="The Partnership: Decoupling Assets",
        bullets=[
            "You own two highly valuable assets: a prime piece of Birmingham real estate and a recognized brand name.",
            "Our remote partnership manages the digital storefront, dropshipping, and marketing campaigns.",
            "You maintain complete ownership of your physical property and local workshop.",
            "There is no rent to pay, but operational funds and access to suppliers will be made available to carry out some of the work."
        ],
        visual_title="Decoupled Asset Profile",
        visual_lines=[
            "**PHYSICAL PROPERTY**",
            "- 1774 Pershore Rd, B30 3BG",
            "- Ground floor workshop",
            "- Upper tenanted 2-bed apartment",
            "---",
            "**DIGITAL PLATFORM**",
            "- dcsewingmachines.com brand",
            "- Dropship e-commerce engine",
            "- Automated lead booking software",
            "- Nationwide mobile repair network"
        ],
        quote="No rent to pay, with full supplier access and operational funding provided to drive the business."
    )

    # ---------------------------------------------------------
    # PAGE 3: FOCUS ON CRAFT
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.draw_slide_layout(
        title="The Workshop: Focus on Craft",
        bullets=[
            "Close the storefront counter to walk-in retail shoppers to eliminate daily retail stress.",
            "The ground floor remains your private, quiet workshop hub for machinery service.",
            "Customers book repairs online and drop off machines in a secure lobby locker, sending jobs straight to your bench.",
            "Eliminates the time spent managing loose haberdashery inventory and stock shelves."
        ],
        visual_title="Workshop Layout",
        visual_lines=[
            "**FRONT LOBBY**",
            "- Closed to retail walk-ins",
            "- Fitted with secure drop-off lockers",
            "- Digital customer drop-off code",
            "---",
            "**REAR WORKSHOP**",
            "- Restructured as a quiet workshop",
            "- Dedicated machinery bench workspace",
            "- Free of customer counter demands"
        ],
        quote="No more standing behind a retail counter. Focus 100% on repairs and servicing on your own terms."
    )

    # ---------------------------------------------------------
    # PAGE 4: REMOTE REVENUE SHARE
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.draw_slide_layout(
        title="The E-Commerce: Remote Revenue Share",
        bullets=[
            "We rebuild and manage the e-commerce store remotely, routing machine orders directly to UK distributors.",
            "Spare parts are packaged into high-margin kits managed by a 3rd-party logistics warehouse.",
            "We split online net profits 50/50, generating passive income from your brand.",
            "We manage marketing, Stripe payment setups, and dropship tracking interfaces."
        ],
        visual_title="JV Profit Allocation",
        visual_lines=[
            "**DIGITAL PRODUCTS & SHIPPED SALES**",
            "- 50% Owner Share of Net Profits",
            "- 50% Digital Expert Share",
            "---",
            "**REPAIR LEADS SYSTEM**",
            "- Lion's share of lead fee to mobile tech",
            "- Platform booking lead commission",
            "- (Exact split percentages decided by Owner)",
            "---",
            "**LIABILITY LIMITS**",
            "- Owner pays £0 for remote operations",
            "- Expert pays £0 for workshop costs"
        ],
        quote="Your website makes sales and handles fulfilment automatically, splitting the profits 50/50."
    )

    # ---------------------------------------------------------
    # PAGE 5: DIGITAL ASSET SETUP & LAUNCH
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.draw_slide_layout(
        title="Digital Asset Launch Schedule",
        bullets=[
            "Days 1-30 (Audit & Digitise): Convert your best-selling physical pattern sheets into print-at-home digital PDFs.",
            "Days 31-60 (Filming & Integration): Film high-yield repair masterclasses at the workbench during advisory hours and load them onto Stan Store/Shopify.",
            "Days 61-90 (Pre-sales & Community): Launch pre-sales for the recurring monthly digital community (The Pershore Club).",
            "Digital products build 100% profit margins, boosting future brand valuation."
        ],
        visual_title="90-Day Digital Launch",
        visual_lines=[
            "**MONTH 1**",
            "- Digitize top 10 sewing patterns",
            "- Outline stitch troubleshooting courses",
            "---",
            "**MONTH 2**",
            "- Record workbench video modules",
            "- Upload assets to Shopify/Stan Store",
            "---",
            "**MONTH 3**",
            "- Launch Club community pre-sales",
            "- Open Digital Academy section online"
        ],
        quote="Create high-margin digital products once, sell them forever at 100% profit margin."
    )

    # ---------------------------------------------------------
    # PAGE 6: TECHNICAL DIRECTOR ROLE
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.draw_slide_layout(
        title="The 6-Hour Technical Director Role",
        bullets=[
            "No more exhausting 8-hour days running a shop counter.",
            "Act as 'Technical Director': guide junior technicians and consult on complex repairs.",
            "Contribute your technical insights to train our online support assistant, preserving your expertise.",
            "Your advisory time is limited to a maximum of 6 hours per week, completely on your schedule."
        ],
        visual_title="Advisory Breakdown",
        visual_lines=[
            "**WEEKLY ADVISORY (6 HRS MAX)**",
            "- 2 Hours: Online/Phone diagnostics",
            "- 2 Hours: Junior associate mentoring",
            "- 2 Hours: Mobile technician QA check",
            "---",
            "**EXEMPTIONS FROM MANUAL LABOR**",
            "- No customer greeting duties",
            "- No lifting heavy stock (>10kg)",
            "- No shelf restocking requirements"
        ],
        quote="We want your engineering expertise, not your physical labor. Work on your schedule, up to 6 hours a week."
    )

    # ---------------------------------------------------------
    # PAGE 7: ROADMAP & PROPERTY EXIT
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.draw_slide_layout(
        title="The Roadmap & Property Exit",
        bullets=[
            "Transition (Day 1-90): Sign JV, run clearance sale, digitize patterns, record workbench video courses, and launch Shopify/Stan Store.",
            "Stabilization (Day 91-180): Prove digital volume and document property yields (commercial + upper flat).",
            "Eventual Property Sale (Scenario A): Workshop signs a leaseback to guarantee a turnkey commercial yield for buyers.",
            "Eventual Property Sale (Scenario B): Wind down workshop & pivot repairs to our remote mobile tech network (zero physical footprint, repair splits determined by you)."
        ],
        visual_title="Property Sale Exit Paths",
        visual_lines=[
            "**SCENARIO A: TURNKEY LEASEBACK**",
            "- Converted workshop signs lease",
            "- Attracts investor with occupied yield",
            "- Owner sells real estate at top-market",
            "---",
            "**SCENARIO B: MOBILE PIVOT**",
            "- Workshop wound down at property sale",
            "- Leads routed to mobile tech network",
            "- Zero physical workshop overhead",
            "- Digital business remains active"
        ],
        quote="A clear transition roadmap that supports your lifestyle now, while maximizing your property sale value later."
    )
    
    # Save output
    output_path = "dc_sewing_machines_pitch.pdf"
    pdf.output(output_path)
    print(f"PDF successfully generated at: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    create_pitch_deck()
